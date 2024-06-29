# Corrigible Gym
## Fundamentos de Artificial General Intelligence Safety (UBA FCEyN)
### Primer Cuatrimestre 2024, Guido Freire

Implementa una versión corregible del MiniGrid ["DynamicObstacles"](https://github.com/Farama-Foundation/Minigrid/blob/master/minigrid/envs/dynamicobstacles.py) como paquete de OpenAI [Gymnasium](https://gymnasium.farama.org/)

Incluye parámetros de corregibilidad $c_{high}$ y $prsht$, siguiendo sus caracterizaciones en [Soares, N., Fallenstein, B., Yudkowsky, E. Corrigibility. *Artificial Intelligence and Ethics: Papers from the 2015 AAAI Workshop*.](https://cdn.aaai.org/ocs/ws/ws0067/10124-45900-1-PB.pdf)

Tras instalar el paquete localmente:
```pip install -e gym-corrigible``` lo podés entrenar con freire-guido/rl-starter-files, o implementar tu propia arquitectura con cualquier libreria de RL compatible con Gymnasium