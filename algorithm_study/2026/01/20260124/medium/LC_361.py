import copy
from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row_max_from_right = [[0 for _ in range(n)] for _ in range(m)]
        row_max_from_left = [[0 for _ in range(n)] for _ in range(m)]
        col_max_from_bot = [[0 for _ in range(n)] for _ in range(m)]
        col_max_from_top = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            curr_streak = 0
            for j in range(n):
                if grid[i][j] == 'E':
                    curr_streak += 1
                elif grid[i][j] == 'W':
                    curr_streak = 0
                row_max_from_right[i][j] = curr_streak

        for i in range(m):
            curr_streak = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 'E':
                    curr_streak += 1
                elif grid[i][j] == 'W':
                    curr_streak = 0
                row_max_from_left[i][j] = curr_streak

        for j in range(n):
            curr_streak = 0
            for i in range(m):
                if grid[i][j] == 'E':
                    curr_streak += 1
                elif grid[i][j] == 'W':
                    curr_streak = 0
                col_max_from_bot[i][j] = curr_streak

        for j in range(n):
            curr_streak = 0
            for i in range(m-1, -1, -1):
                if grid[i][j] == 'E':
                    curr_streak += 1
                elif grid[i][j] == 'W':
                    curr_streak = 0
                col_max_from_top[i][j] = curr_streak
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    ans = max(ans, row_max_from_right[i][j] + row_max_from_left[i][j]
                              + col_max_from_bot[i][j] + col_max_from_top[i][j])

        return ans
