class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7

        dp = [1] * 5
        for i in range(1, n):
            new_dp = [0] * 5
            new_dp[0] += dp[1]
            new_dp[1] += (dp[0] + dp[2]) % mod
            new_dp[2] += (dp[0] + dp[1] + dp[3] + dp[4]) % mod
            new_dp[3] += (dp[2] + dp[4]) % mod
            new_dp[4] += dp[0]
            dp = new_dp

        return sum(dp) % mod
