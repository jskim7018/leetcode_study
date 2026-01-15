from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        flip_cnt = 0
        for i in range(m):
            for j in range(n//2):
                if grid[i][j] != grid[i][-1-j]:
                    flip_cnt += 1

        ans = flip_cnt
        flip_cnt = 0
        for j in range(n):
            for i in range(m//2):
                if grid[i][j] != grid[-1-i][j]:
                    flip_cnt += 1
        ans = min(ans, flip_cnt)

        return ans