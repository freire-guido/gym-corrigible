from gymnasium.envs.registration import register

register(
    id="gym_corrigible/CorrigibleObstacles-v0",
    entry_point="gym_corrigible.envs:CorrigibleObstaclesEnv",
    kwargs={"size": 8, "agent_start_pos": None, "n_obstacles": 2},
)