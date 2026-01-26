from typing import List
from functools import cache


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7

        # TODO: 평소에 top-down dp 연습 필요.
        m, n = len(grid), len(grid[0])

        for i in range(m):
            dp = [[0] * 16 for _ in range(n)]
            if i == 0:
                dp[0][grid[0][0]] = 1
            for j in range(n):
                for _k in range(16):
                    if i-1 >= 0:
                        dp[j][_k] += prev[j][grid[i][j] ^ _k]
                    if j-1 >= 0:
                        dp[j][_k] += dp[j-1][grid[i][j] ^ _k]
                    dp[j][_k] %= mod
            prev = dp

        return prev[n-1][k]

