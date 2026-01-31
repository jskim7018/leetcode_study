from typing import List
from functools import cache


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        @cache
        def dp(i: int, j: int) -> int:
            ret = 0
            if j + 1 < n:
                if i-1 >= 0 and grid[i-1][j+1] > grid[i][j]:
                    ret = max(ret, dp(i-1, j+1) + 1)
                if grid[i][j+1] > grid[i][j]:
                    ret = max(ret, dp(i, j+1) + 1)
                if i + 1 < m and grid[i+1][j+1] > grid[i][j]:
                    ret = max(ret, dp(i+1, j+1) + 1)
            return ret

        ans = 0
        for i in range(m):
            ans = max(ans, dp(i, 0))

        return ans
