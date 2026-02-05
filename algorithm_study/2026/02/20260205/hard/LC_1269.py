class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7

        prev_dp = [1]
        for i in range(1, steps+1):
            new_dp = [0] * min(arrLen, (i + 1))
            for j in range(len(new_dp)):
                if j < len(prev_dp):
                    new_dp[j] = prev_dp[j]
                if j - 1 >= 0:
                    new_dp[j] += prev_dp[j-1]
                if j + 1 < len(prev_dp):
                    new_dp[j] += prev_dp[j+1]
                new_dp[j] %= mod
            prev_dp = new_dp

        return prev_dp[0]