<div align="center">

# Amir Ata Ghaffarian

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amir-ata-ghaffarian/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:amirata.ghafarian@gmail.com)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Amirata051)

</div>

---

## About Me

Research Intern at **OIST** (Okinawa Institute of Science and Technology), working on self-supervised deep learning for comparative genomics under [Prof. Nicholas Luscombe](https://www.oist.jp/research/nicholas-luscombe).

My core interests lie at the intersection of **World Models**, **Reinforcement Learning**, **Robotics**, and **Embodied AI** — with a side of Computational Biology.

```python
from dataclasses import dataclass, field
from typing import Literal

@dataclass
class AmiRata:
    name: str = "Amir Ata Ghaffarian"
    location: str = "Onna, Okinawa 🇯🇵"
    affiliation: str = "OIST — Genomics & Regulatory Systems Unit"

    interests: list[str] = field(default_factory=lambda: [
        "World Models & Reinforcement Learning",
        "Robotics & Embodied AI",
        "Self-Supervised Learning",
        "Computational Biology",
    ])

    current_work: dict = field(default_factory=lambda: {
        "project": "Scrambling in the Tree of Life",
        "model":   "Set Transformer + VICReg on genomic point clouds",
        "compute": "4× A100 GPUs | DDP | BF16 | Flash Attention 2",
    })

    stack: dict = field(default_factory=lambda: {
        "ml":    ["PyTorch", "HuggingFace", "JAX"],
        "infra": ["Slurm", "Singularity", "Docker", "Kubernetes"],
        "langs": ["Python", "Go", "C++"],
    })

    def is_available_for_phd(self) -> bool:
        return True   # starting 2027 🎓

    def __repr__(self) -> str:
        return f"Building things that learn. Looking for a PhD. {self.location}"


if __name__ == "__main__":
    me = AmiRata()
    print(me)
```

---

## Research

| | |
|---|---|
| 🧬 **OIST** (2026–present) | Self-supervised learning on pairwise genomic alignments — Set Transformer + VICReg to classify structural rearrangement topology across the tree of life |
| ⚙️ **Sharif University** (2025) | Diffusion models + Transformers for predictive maintenance (bearing & battery RUL estimation) |

---

## Tech Stack

**ML / Research**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

**Infrastructure**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)

---

## GitHub Stats

<div align="center">

![Amir's GitHub stats](https://github-readme-stats.vercel.app/api?username=amirata051&show_icons=true&theme=github_dark&hide_border=true&include_all_commits=true&count_private=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=amirata051&layout=compact&theme=github_dark&hide_border=true&langs_count=6)

</div>

---

<div align="center">

*"The question is not whether intelligent machines can have feelings, but whether machines without feelings can ever be truly intelligent."*

</div>
