from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def toggle_row(row_idx):
            # implement row toggle.
            for j in range(n):
                grid[row_idx][j] ^= 1

        for i in range(m):
            if grid[i][0] == 0:
                toggle_row(i)

        score = 0
        mult = 1
        for j in range(n):
            ones_cnt = 0
            zeros_cnt = 0
            for i in range(m):
                if grid[i][-j-1] == 0:
                    zeros_cnt += 1
                else:
                    ones_cnt += 1
            score += max(zeros_cnt, ones_cnt) * mult
            mult *= 2
        return score
