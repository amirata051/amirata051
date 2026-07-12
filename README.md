```python
import torch
import torch.nn as nn


class Amir(nn.Module):
    """CS @ Tehran Polytechnic  ·  Research Intern @ OIST"""

    def __init__(self):
        super().__init__()
        self.interests = [
            "self-supervised learning", "world models",
            "reinforcement learning", "embodied ai", "ai for genomics",
        ]
        self.encoder   = SetTransformer()        # genomes -> latent space
        self.objective = VICReg()                # learning without labels
        self.optimizer = torch.optim.AdamW(self.parameters(), lr=3e-4)
        self.epsilon   = 0.3                     # still in exploration phase

    def forward(self, reality):
        z = self.encoder(reality.observe())      # compress the world
        return self.reason(z)                    # then act on it

    def loss(self):
        return curiosity(w=1.0) + depth(w=0.8) - stagnation(w=float("inf"))
```

<div align="center">

[![Homepage](https://img.shields.io/badge/Homepage-181717?style=flat&logo=githubpages&logoColor=white)](https://amirata051.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/amirata-ghaffarian)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:amirata.ghafarian@gmail.com)
[![OIST](https://img.shields.io/badge/OIST-003E69?style=flat&logoColor=white)](https://www.oist.jp)

</div>

---

### 🔬 What I'm working on

I'm a Research Intern in **[Prof. Nicholas Luscombe's](https://www.oist.jp/research/research-units/gars) Genomics & Regulatory Systems Unit at OIST**, working at the intersection of self-supervised learning and genomics.

- 🧬 **Scrambling in the Tree of Life** — training a **Set Transformer** with a **VICReg** objective on point-cloud representations of pairwise genomic alignments across **~300K genome pairs**, on **4× A100** GPUs. Targeting a **NeurIPS 2026** workshop submission.
- 🌍 Broadly curious about **world models, RL, and embodied AI** — how agents can compress reality into useful latent spaces and act in it.
- 🎯 **Next up:** pursuing a **PhD** in world models & embodied AI.

Before OIST, I researched diffusion-based approaches for predictive maintenance at Sharif, and spent time in industry on backend & SRE (Go, Kafka, Docker).

---

### 🛠️ Tech Stack

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)

**ML / Deep Learning**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

**Systems & HPC**

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Slurm](https://img.shields.io/badge/Slurm-2C3E50?style=flat&logoColor=white)
![Singularity](https://img.shields.io/badge/Singularity-1A2A3A?style=flat&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apachekafka&logoColor=white)

**Data**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)

---

### 📊 GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=amirata051&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=amirata051&layout=compact&theme=tokyonight&hide_border=true&langs_count=8&hide=jupyter%20notebook" />

<img src="https://streak-stats.demolab.com/?user=amirata051&theme=tokyonight&hide_border=true" height="165" />

</div>

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/amirata051/amirata051/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/amirata051/amirata051/output/github-snake.svg" />
  <img alt="github-snake" src="https://raw.githubusercontent.com/amirata051/amirata051/output/github-snake.svg" />
</picture>

</div>
