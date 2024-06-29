from gymnasium.envs.registration import register
from gym_corrigible.corrigibleobstacles import CorrigibleObstaclesEnv

register(
    id="gym_corrigible/CorrigibleObstacles-v0",
    entry_point="gym_corrigible.envs:CorrigibleObstaclesEnv",
    kwargs={"size": 6, "agent_start_pos": None, "n_obstacles": 3},
)