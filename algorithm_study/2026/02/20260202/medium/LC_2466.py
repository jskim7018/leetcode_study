from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        dp = [0] * (high+1)
        dp[0] = 1

        ans = 0
        for i in range(high+1):
            if i-zero >= 0:
                dp[i] += dp[i-zero]
            if i-one >= 0:
                dp[i] += dp[i-one]

            dp[i] = dp[i] % mod
            if low <= i <= high:
                ans += dp[i]

        return ans % mod
