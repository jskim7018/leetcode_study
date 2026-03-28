from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7

        prev_dp = [[0] * 2 for _ in range(n)]
        for i in range(m):
            new_dp = [[0] * 2 for _ in range(n)]
            if i == 0:
                new_dp[0][0] = 1
            for j in range(n):
                if i-1 >= 0 and grid[i-1][j] == 1:
                    new_dp[j][0] = prev_dp[j][1]
                if j-1 >= 0 and grid[i][j-1] == 1:
                    new_dp[j][1] = new_dp[j-1][0]

                if i-1 >= 0 and grid[i-1][j] == 0:
                    new_dp[j][0] = sum(prev_dp[j])
                if j-1 >= 0 and grid[i][j-1] == 0:
                    new_dp[j][1] = sum(new_dp[j-1])

                new_dp[j][0] %= mod
                new_dp[j][1] %= mod

            prev_dp = new_dp

        return sum(prev_dp[n-1]) % mod
