from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # dp, 위의 꺼의 베스트 혹은 왼쪽의 베스트
        m, n = len(grid), len(grid[0])

        dp = [float('-inf')] * n
        ans = float('-inf')
        for j in range(n):
            if j - 1 >= 0:
                cand = grid[0][j] - grid[0][j - 1]
                if dp[j - 1] > 0:
                    cand += dp[j - 1]
                dp[j] = max(dp[j], cand)
                ans = max(ans, dp[j])

        for i in range(m):
            new_dp = [float('-inf')] * n
            for j in range(n):
                if i-1 >= 0:
                    cand = grid[i][j] - grid[i-1][j]
                    if dp[j] > 0:
                        cand += dp[j]
                    new_dp[j] = max(new_dp[j], cand)
                if j-1 >= 0:
                    cand = grid[i][j] - grid[i][j-1]
                    if new_dp[j-1] > 0:
                        cand += new_dp[j-1]
                    new_dp[j] = max(new_dp[j], cand)
                ans = max(ans, new_dp[j])
            dp = new_dp

        return ans
