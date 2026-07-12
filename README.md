<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8B5CF6,50:6366F1,100:38BDF8&height=200&section=header&text=Amir%20Ata%20Ghaffarian&fontSize=48&fontColor=FFFFFF&fontAlignY=36&desc=AI%20%2F%20ML%20Researcher%20%C2%B7%20World%20Models%20%C2%B7%20Embodied%20AI&descSize=18&descAlignY=58" width="100%" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1000&color=8B5CF6&center=true&vCenter=true&width=650&lines=Research+Intern+%40+OIST%2C+Japan+%F0%9F%87%AF%F0%9F%87%B5;Self-Supervised+Learning+%C2%B7+VICReg+%C2%B7+JEPA;World+Models+%E2%80%A2+RL+%E2%80%A2+Robotics;Turning+latent+space+into+action..." alt="Typing SVG" />
</a>

<br/>

[![Homepage](https://img.shields.io/badge/Homepage-1a1a2e?style=for-the-badge&logo=githubpages&logoColor=8B5CF6)](https://amirata051.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/amirata-ghaffarian)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:amirata.ghafarian@gmail.com)
[![OIST](https://img.shields.io/badge/OIST-003E69?style=for-the-badge&logoColor=white)](https://www.oist.jp)

<img src="https://komarev.com/ghpvc/?username=amirata051&style=for-the-badge&color=8B5CF6&label=PROFILE+VIEWS" alt="profile views" />

</div>

---

```python
from future import Research
import torch
import torch.nn as nn


class AmirAta(nn.Module):
    """AI / ML Researcher · World Models · Embodied AI"""

    def __init__(self):
        super().__init__()
        self.role      = "Research Intern @ OIST, Japan 🇯🇵"
        self.focus     = "self-supervised learning for genomics (VICReg · JEPA · GNNs)"
        self.education = "B.Sc. Computer Science, Amirkabir — GPA 4.0/4.0"
        self.interests = ["World Models", "RL", "Robotics",
                          "Embodied AI", "Neuroscience", "Comp. Biology"]
        self.epsilon   = 0.3  # still in the exploration phase

    def forward(self, obs: Tensor) -> Action:
        z = self.world_model(obs)   # compress reality into a latent space
        return self.policy(z)       # ...then act on it

    def loss(self) -> Tensor:
        return (
              curiosity(weight=1.0)
            + depth(weight=0.8)
            - stagnation(weight=float("inf"))
        )
```

---

<!-- ## 🧠 About Me

- 🔬 **Research Intern** at the **Okinawa Institute of Science & Technology (OIST)**, in the *Genomics & Regulatory Systems Unit* — decoding genomic rearrangement patterns with **self-supervised learning** (VICReg, JEPA, Transformers) and **Graph Neural Networks**, running an end-to-end pipeline on an **HPC cluster** with Slurm & Singularity.
- 🎓 Computer Science graduate from **Amirkabir University of Technology (Tehran Polytechnic)** — **GPA 4.0/4.0**, ranked **top 5%** in the CS cohort.
- 🏆 Ranked in the **top 0.3% (464 / 150,000)** in Iran's National University Entrance Exam.
- 🧩 Previously researched **predictive maintenance** (transformers + diffusion) @ **Sharif CISDS**, built ad-serving infra @ **Yektanet**, and trained in **SRE** @ **Neshan**.
- 🌱 Currently going deeper into **World Models, RL, and Embodied AI**.
- 👨‍🏫 Long-time **Teaching Assistant** (ML, AI, Algorithms, Image Processing, OS) and **Python mentor**.

--- -->

<!-- ## 🛠️ Tech Arsenal

<div align="center">

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)

**Machine Learning & Deep Learning**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

**Backend & Web**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Gin](https://img.shields.io/badge/Gin-008ECF?style=for-the-badge&logo=gin&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

**Databases & Storage**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white)
![FalkorDB](https://img.shields.io/badge/FalkorDB-FF1744?style=for-the-badge&logoColor=white)

**DevOps, Infra & HPC**

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab%20CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Slurm](https://img.shields.io/badge/Slurm-0B5394?style=for-the-badge&logoColor=white)
![Singularity](https://img.shields.io/badge/Singularity-1D2B3A?style=for-the-badge&logoColor=white)

</div>

---

## 🚀 Featured Projects

<div align="center">

| Project | Description | Stack |
|:--------|:------------|:------|
| 🕸️ **[Knowledge Graph Generator](https://github.com/amirata051)** | Generates knowledge graphs from heterogeneous sources; real-time & idempotent by design | `Python` · `FalkorDB` · `Kafka` · `MinIO` · `Redis` |
| 🔧 **[DiffRUL-CMAPSS](https://github.com/amirata051)** | Diffusion-based data augmentation for aero-engine RUL estimation (LSTM + Transformer + DDPM) | `PyTorch` · `Diffusion` |
| 🔍 **[Search Engine](https://github.com/amirata051)** | IR system with TF-IDF & ParsBERT, K-Means clustering and FAISS retrieval | `Python` · `ParsBERT` · `FAISS` |
| 🧬 **[Deep Learning Projects](https://github.com/amirata051)** | Implementations of GANs, KANs and MLPs, tuned for performance & deployment | `PyTorch` |
| 📄 **[Applicant Tracking System](https://github.com/amirata051)** | NLP web app ranking CVs via SentenceTransformers + cosine similarity | `Flask` · `Docker` · `NLP` |
| 📢 **[Dotanet Ad Server](https://github.com/amirata051)** | Scalable ad platform: retrieval, auctions & real-time click/impression tracking | `Go` · `PostgreSQL` · `Kafka` |

</div>

--- -->

## 📊 GitHub Analytics

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=amirata051&show_icons=true&count_private=true&include_all_commits=true&hide_border=true&title_color=8B5CF6&icon_color=38BDF8&text_color=C9D1D9&bg_color=0D1117" />
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=amirata051&layout=compact&langs_count=8&hide_border=true&title_color=8B5CF6&text_color=C9D1D9&bg_color=0D1117" />

<br/>

<img src="https://streak-stats.demolab.com?user=amirata051&hide_border=true&background=0D1117&ring=8B5CF6&fire=38BDF8&currStreakLabel=8B5CF6&sideNums=C9D1D9&sideLabels=C9D1D9&dates=8B949E&stroke=8B5CF6&currStreakNum=C9D1D9&dayLabels=C9D1D9" />

<br/>

<img src="https://github-profile-trophy.vercel.app/?username=amirata051&theme=onedark&no-frame=true&no-bg=true&column=7&margin-w=4&margin-h=4" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=amirata051&bg_color=0D1117&color=8B5CF6&line=38BDF8&point=FFFFFF&area=true&hide_border=true" width="100%" />

</div>

---
<!-- 
## 🎓 Education & Highlights

- 🏛️ **B.Sc. in Computer Science** — Amirkabir University of Technology (Tehran Polytechnic), 2020–2025
- 📈 **GPA 4.0/4.0** (18.97/20) · Final-year GPA **19.60/20**
- 🥇 **Top 0.3%** (464 / 150,000) — National University Entrance Exam (Mathematics)
- 🎖️ **Machine Learning Specialization** — DeepLearning.AI & Stanford
- 🧪 **Neuromatch Deep Learning Course** · ☁️ **Cloud Practitioner** — Cloud Academy

--- -->

## 🐍 Watch the Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/amirata051/amirata051/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/amirata051/amirata051/output/github-snake.svg" />
  <img alt="github-snake" src="https://raw.githubusercontent.com/amirata051/amirata051/output/github-snake.svg" width="100%" />
</picture>

</div>

---

<div align="center">

*“I like deep neural nets.”*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:38BDF8,50:6366F1,100:8B5CF6&height=120&section=footer" width="100%" />

</div>
