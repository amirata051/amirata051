#!/usr/bin/env python3
"""
Refresh the Uptime line in dark_mode.svg / light_mode.svg.

Runs daily from .github/workflows/update-stats.yml. Uptime counts from
Amir Ata's birthday, so no API access is needed.
"""

import datetime
import re
import sys

BIRTHDAY = datetime.date(2002, 4, 13)
SVG_FILES = ("dark_mode.svg", "light_mode.svg")


def uptime_string(born, today=None):
    today = today or datetime.date.today()
    years = today.year - born.year
    months = today.month - born.month
    days = today.day - born.day
    if days < 0:
        months -= 1
        prev_month_end = datetime.date(today.year, today.month, 1) - datetime.timedelta(days=1)
        days += prev_month_end.day
    if months < 0:
        years -= 1
        months += 12

    def plural(n, unit):
        return f"{n} {unit}{'' if n == 1 else 's'}"

    return f"{plural(years, 'year')}, {plural(months, 'month')}, {plural(days, 'day')}"


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
    values = {"age_data": uptime_string(BIRTHDAY)}
    for path in SVG_FILES:
        update_svg(path, values)
    print("Updated uptime:", values["age_data"])


if __name__ == "__main__":
    main()
