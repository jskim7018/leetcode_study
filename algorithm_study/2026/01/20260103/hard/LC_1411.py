class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7

        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] * 2 + dp[i - 1][1] * 2
            dp[i][0] %= mod
            dp[i][1] = dp[i - 1][0] * 2 + dp[i - 1][1] * 3
            dp[i][1] %= mod

        return (dp[n-1][0] * 6 + dp[n-1][1] * 6) % mod
