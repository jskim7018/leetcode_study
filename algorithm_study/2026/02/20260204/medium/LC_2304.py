from typing import List
from copy import copy


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0]
        for i in range(1, m):
            new_dp = copy(grid[i])
            for j in range(n):
                minim = float('inf')
                for k in range(n):
                    minim = min(minim, dp[k] + moveCost[grid[i-1][k]][j])
                new_dp[j] += minim
            dp = new_dp
        return min(dp)
