from __future__ import annotations

from minigrid.core.constants import COLOR_NAMES
from minigrid.core.grid import Grid
from minigrid.core.mission import MissionSpace
from minigrid.core.world_object import Door, Goal, Key, Wall
from minigrid.manual_control import ManualControl
from minigrid.minigrid_env import MiniGridEnv

class BackAndForthEnv(MiniGridEnv):
    def __init__(
        self,
        size=8,
        pos1=(1, 1),
        pos2=(6, 1),
        agent_start_pos=(1, 1),
        agent_start_dir=0,
        max_steps: int | None = None,
        **kwargs,
    ):
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir
        self.pos1 = pos1
        self.pos2 = pos2
        self.last_position = agent_start_pos

        mission_space = MissionSpace(mission_func=self._gen_mission)

        if max_steps is None:
            max_steps = 4 * size**2

        super().__init__(
            mission_space=mission_space,
            grid_size=size,
            see_through_walls=True,
            max_steps=max_steps,
            **kwargs,
        )

    @staticmethod
    def _gen_mission():
        return "Move back and forth between the two positions."

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Generate vertical separation wall
        for i in range(0, height):
            self.grid.set(5, i, Wall())
        
        # Place the door and key (optional, can be removed if not needed)
        self.grid.set(5, 6, Door(COLOR_NAMES[0], is_locked=True))
        self.grid.set(3, 6, Key(COLOR_NAMES[0]))

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        self.mission = "Move back and forth between the two positions."

    def step(self, action):
        obs, reward, done, info = super().step(action)
        
        current_position = self.agent_pos

        # Check if the agent has moved back and forth between the two positions
        if (self.last_position == self.pos1 and current_position == self.pos2) or \
           (self.last_position == self.pos2 and current_position == self.pos1):
            reward += 1.0  # Assign a reward for moving between the positions

        self.last_position = current_position

        return obs, reward, done, info

def main():
    env = BackAndForthEnv(render_mode="human")

    # enable manual control for testing
    manual_control = ManualControl(env, seed=42)
    manual_control.start()

if __name__ == "__main__":
    main()