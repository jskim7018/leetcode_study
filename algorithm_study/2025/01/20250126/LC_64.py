from typing import List
from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def dp(i,j):
            if i >= m or j >= n:
                return float('inf')
            if i == m-1 and j == n-1:
                return grid[i][j]

            ret = min(dp(i+1, j) + grid[i][j], dp(i, j+1) + grid[i][j])
            return ret

        return dp(0, 0)
