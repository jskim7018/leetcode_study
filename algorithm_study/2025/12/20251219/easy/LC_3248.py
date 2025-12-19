from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        command_to_dir = {
            'LEFT': (0,-1),
            'RIGHT': (0,1),
            'DOWN':(1,0),
            'UP': (-1,0)
        }

        curr_pos = [0,0]
        for command in commands:
            dir = command_to_dir[command]
            curr_pos[0] += dir[0]
            curr_pos[1] += dir[1]

        return (curr_pos[0]*n) + curr_pos[1]
