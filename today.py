#!/usr/bin/env python3
"""
Refresh dark_mode.svg / light_mode.svg with live GitHub stats.

Runs from .github/workflows/update-stats.yml. Authenticates with the
ACCESS_TOKEN secret (a classic PAT, for private-contribution counts) when
present, otherwise falls back to the workflow's GITHUB_TOKEN.
"""

import datetime
import os
import re
import sys
import time

import requests

USER = os.environ.get("USER_NAME", "amirata051")
TOKEN = os.environ.get("ACCESS_TOKEN") or os.environ.get("GITHUB_TOKEN")
API = "https://api.github.com"
HEADERS = {"Authorization": f"bearer {TOKEN}"} if TOKEN else {}
SVG_FILES = ("dark_mode.svg", "light_mode.svg")


def graphql(query, variables):
    for attempt in range(4):
        r = requests.post(
            f"{API}/graphql",
            json={"query": query, "variables": variables},
            headers=HEADERS,
            timeout=30,
        )
        if r.status_code == 200:
            payload = r.json()
            if "errors" not in payload:
                return payload["data"]
            print("GraphQL errors:", payload["errors"], file=sys.stderr)
        else:
            print(f"GraphQL HTTP {r.status_code}: {r.text[:200]}", file=sys.stderr)
        time.sleep(2**attempt)
    raise RuntimeError("GraphQL query failed after retries")


def fetch_overview():
    query = """
    query($login: String!, $cursor: String) {
      user(login: $login) {
        createdAt
        followers { totalCount }
        following { totalCount }
        repositoriesContributedTo(
          contributionTypes: [COMMIT, PULL_REQUEST, REPOSITORY, PULL_REQUEST_REVIEW]
        ) { totalCount }
        repositories(first: 100, after: $cursor, ownerAffiliations: OWNER) {
          totalCount
          pageInfo { hasNextPage endCursor }
          nodes { name isFork stargazerCount }
        }
      }
    }"""
    cursor = None
    nodes = []
    while True:
        user = graphql(query, {"login": USER, "cursor": cursor})["user"]
        repos = user["repositories"]
        nodes.extend(repos["nodes"])
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    return {
        "created_at": datetime.datetime.fromisoformat(
            user["createdAt"].replace("Z", "+00:00")
        ),
        "followers": user["followers"]["totalCount"],
        "following": user["following"]["totalCount"],
        "contributed": user["repositoriesContributedTo"]["totalCount"],
        "repo_count": repos["totalCount"],
        "stars": sum(n["stargazerCount"] for n in nodes),
        "source_repos": [n["name"] for n in nodes if not n["isFork"]],
    }


def fetch_total_commits(created_at):
    """All-time commit contributions, summed year by year."""
    query = """
    query($login: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $login) {
        contributionsCollection(from: $from, to: $to) {
          totalCommitContributions
          restrictedContributionsCount
        }
      }
    }"""
    now = datetime.datetime.now(datetime.timezone.utc)
    total = 0
    for year in range(created_at.year, now.year + 1):
        start = max(created_at, datetime.datetime(year, 1, 1, tzinfo=datetime.timezone.utc))
        end = min(now, datetime.datetime(year, 12, 31, 23, 59, 59, tzinfo=datetime.timezone.utc))
        coll = graphql(
            query,
            {"login": USER, "from": start.isoformat(), "to": end.isoformat()},
        )["user"]["contributionsCollection"]
        total += coll["totalCommitContributions"] + coll["restrictedContributionsCount"]
    return total


def fetch_loc(repo_names):
    """Lines added/deleted by USER across their source repos (REST contributor stats)."""
    added = deleted = 0
    failures = 0
    for name in repo_names:
        url = f"{API}/repos/{USER}/{name}/stats/contributors"
        stats = None
        for _ in range(8):
            r = requests.get(url, headers=HEADERS, timeout=30)
            if r.status_code == 200:
                stats = r.json()
                break
            if r.status_code == 202:  # stats being computed, try again
                time.sleep(3)
                continue
            print(f"LOC: {name} -> HTTP {r.status_code}", file=sys.stderr)
            break
        if not isinstance(stats, list):
            failures += 1
            continue
        for contributor in stats:
            author = contributor.get("author") or {}
            if author.get("login", "").lower() == USER.lower():
                for week in contributor["weeks"]:
                    added += week["a"]
                    deleted += week["d"]
    return added, deleted, failures


def uptime_string(created_at):
    now = datetime.datetime.now(datetime.timezone.utc)
    years = now.year - created_at.year
    months = now.month - created_at.month
    days = now.day - created_at.day
    if days < 0:
        months -= 1
        prev_month_end = datetime.date(now.year, now.month, 1) - datetime.timedelta(days=1)
        days += prev_month_end.day
    if months < 0:
        years -= 1
        months += 12
    def plural(n, unit):
        return f"{n} {unit}{'' if n == 1 else 's'}"
    return f"{plural(years, 'year')}, {plural(months, 'month')}, {plural(days, 'day')}"


def fmt(n):
    return f"{n:,}"


def update_svg(path, values):
    with open(path, encoding="utf-8") as f:
        svg = f.read()
    for tspan_id, text in values.items():
        pattern = rf'(<tspan[^>]*id="{tspan_id}"[^>]*>)[^<]*(</tspan>)'
        svg, count = re.subn(pattern, lambda m: m.group(1) + text + m.group(2), svg)
        if count == 0:
            print(f"warning: id {tspan_id} not found in {path}", file=sys.stderr)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)


def main():
    info = fetch_overview()
    commits = fetch_total_commits(info["created_at"])
    added, deleted, loc_failures = fetch_loc(info["source_repos"])

    values = {
        "age_data": uptime_string(info["created_at"]),
        "repo_data": fmt(info["repo_count"]),
        "contrib_data": fmt(info["contributed"]),
        "star_data": fmt(info["stars"]),
        "commit_data": fmt(commits),
        "follower_data": fmt(info["followers"]),
        "following_data": fmt(info["following"]),
    }
    if added or deleted:
        values.update(
            loc_data=fmt(added - deleted),
            loc_add_data=fmt(added) + "++",
            loc_del_data=fmt(deleted) + "--",
        )
    elif loc_failures:
        print("LOC unavailable, keeping previous values", file=sys.stderr)

    # dot leaders absorb value-length changes so columns stay aligned
    dot_slots = {
        "repo_dots": (7, "repo_data"),
        "star_dots": (8, "star_data"),
        "commit_dots": (6, "commit_data"),
        "follower_dots": (4, "follower_data"),
        "following_dots": (4, "following_data"),
        "loc_dots": (8, "loc_data"),
    }
    for dots_id, (slot, value_id) in dot_slots.items():
        if value_id in values:
            n = max(2, slot - len(values[value_id]))
            values[dots_id] = " " + "." * n + " "

    for path in SVG_FILES:
        update_svg(path, values)

    print("Updated:", {k: v for k, v in values.items() if k.endswith("_data")})


if __name__ == "__main__":
    main()
