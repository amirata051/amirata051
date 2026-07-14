<div align="center">

<!--
  Neofetch-style profile card. The Uptime line is refreshed daily by
  today.py via .github/workflows/update-stats.yml.
-->

<a href="https://github.com/amirata051">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="dark_mode.svg">
    <source media="(prefers-color-scheme: light)" srcset="light_mode.svg">
    <img alt="Amir Ata Ghaffarian — AI/ML researcher. Terminal-style profile card." src="dark_mode.svg" width="100%">
  </picture>
</a>

[![Homepage](https://img.shields.io/badge/Homepage-1a1a2e?style=for-the-badge&logo=githubpages&logoColor=8B5CF6)](https://amirata051.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/amir-ata-ghaffarian)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:amirata.ghafarian@gmail.com)
[![OIST](https://img.shields.io/badge/OIST-003E69?style=for-the-badge&logoColor=white)](https://www.oist.jp)

</div>

---

```python
from future import Research
import torch
import torch.nn as nn

class AmirAta(nn.Module):
    """AI / ML Researcher"""

    def __init__(self):
        super().__init__()
        self.role      = "Research Intern @ OIST, Japan 🇯🇵"
        self.focus     = "self-supervised learning for genomics (VICReg · JEPA · GNNs)"
        self.education = "B.Sc. Computer Science, Amirkabir — GPA 4.0/4.0"
        self.status    = "applying for PhD positions · starting 2027"
        self.interests = [
            "World Models",
            "RL",
            "Robotics",
            "Embodied AI",
            "Neuroscience",
            "Comp. Biology",
        ]
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
