from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7

        m, n = len(grid), len(grid[0])
        prev_dp = [[0] * k for _ in range(n)]
        for i in range(m):
            curr_dp = [[0] * k for _ in range(n)]
            if i == 0:
                curr_dp[0][grid[0][0] % k] = 1
            for j in range(n):
                for _k in range(k):
                    _mod = (_k + grid[i][j]) % k
                    if i-1 >= 0:
                        curr_dp[j][_mod] += prev_dp[j][_k]
                    if j - 1 >= 0:
                        curr_dp[j][_mod] += curr_dp[j - 1][_k]
                    curr_dp[j][_mod] %= mod
            prev_dp = curr_dp

        return prev_dp[n-1][0]
