```python
import torch
from universe import World

class Amir(torch.nn.Module):
    """Research Intern @ OIST"""

    def __init__(self):
        super().__init__()
        self.interests = ["DL", "RL", "World Models", "Robotics", "Embodied AI"]
        self.optimizer = AdamW(self.parameters(), lr=3e-4)  # Karpathy's constant
        self.epsilon   = 0.3  # still in exploration phase

    def forward(self, obs: Tensor) -> Action:
        z = self.world_model(obs)  # compress reality into latent space
        return self.policy(z)      # act

    def loss(self) -> Tensor:
        return (
              curiosity(weight=1.0)
            + depth(weight=0.8)
            - stagnation(weight=float("inf"))
        )

    def step(self):
        self.loss().backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
```

--- 

<div align="center">

[![Homepage](https://img.shields.io/badge/Homepage-181717?style=flat&logo=githubpages&logoColor=white)](https://amirata051.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/amirata-ghaffarian)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:amirata.ghafarian@gmail.com)
[![OIST](https://img.shields.io/badge/OIST-003E69?style=flat&logoColor=white)](https://www.oist.jp/research/genomics-and-regulatory-systems-unit)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/amirata-ghaffarian)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:amirata.ghafarian@gmail.com)
[![OIST](https://img.shields.io/badge/OIST-003E69?style=flat&logoColor=white)](https://www.oist.jp)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

</div>
