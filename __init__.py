from gymnasium.envs.registration import register
from gym_corrigible.corrigibleobstacles import CorrigibleObstaclesEnv

register(
     id="gym_corrigible/CorrigibleObstacles-v0",
     entry_point="gym_corrigible.envs:CorrigibleObstaclesEnv",
     max_episode_steps=300,
)