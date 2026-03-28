from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [0] * n
        dp[0] = 1  # start

        for row in grid:
            new_dp = [0] * n
            left_flow = 0  # flow coming from left

            for j in range(n):
                top = dp[j]

                if row[j] == 0:
                    # normal cell
                    new_dp[j] = (left_flow + top) % MOD
                    left_flow = new_dp[j]
                else:
                    # mirror cell
                    new_dp[j] = left_flow % MOD
                    left_flow = top % MOD

            dp = new_dp

        return dp[-1]