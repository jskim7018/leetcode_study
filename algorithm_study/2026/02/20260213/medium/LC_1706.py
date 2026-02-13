from typing import List
from collections import defaultdict


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        ball_loc = defaultdict(set)
        for i in range(n):
            ball_loc[i].add(i)

        for i in range(m):
            new_ball_loc = defaultdict(set)
            for loc, ball_set in ball_loc.items():
                if grid[i][loc] == 1 and (loc+1 < n and grid[i][loc+1] == 1):
                    new_ball_loc[loc+1].update(ball_set)
                elif grid[i][loc] == -1 and (loc-1 >= 0 and grid[i][loc-1] == -1):
                    new_ball_loc[loc - 1].update(ball_set)
            ball_loc = new_ball_loc

        ans = [-1]*n
        for drop_idx, balls in ball_loc.items():
            for balls_idx in balls:
                ans[balls_idx] = drop_idx

        return ans
