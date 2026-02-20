from itertools import accumulate


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # simple dp.
        # dp[i][x] += dp[i-1][x-(1~k)]
        # ans = dp[i-1][target]
        mod = 10**9 + 7
        # TODO: Study the stars and bar + inclusion exclusion method
        prev_dp = [0] * (target+1)
        for j in range(1, min(k, target) + 1):
            prev_dp[j] = 1

        for i in range(1, n):  # 30
            print(prev_dp)
            curr_dp = [0] * (target+1)
            # TODO: prefix optimization
            prefix_sum = list(accumulate(prev_dp))
            for j in range(1, target+1):  # 1000
                curr_dp[j] += prefix_sum[j-1]
                if j - k - 1 >= 0:
                    curr_dp[j] -= prefix_sum[j-k-1]
                curr_dp[j] %= mod
            prev_dp = curr_dp
        return prev_dp[target]
