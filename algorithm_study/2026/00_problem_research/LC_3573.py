from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # TODO: 자세히 공부 필요.
        n = len(prices)
        if n == 0:
            return 0

        # Initialize DP
        dp = [[[0, -prices[0], prices[0]] for _ in range(k + 1)] for _ in range(n)]
        # dp[i][t] = [no_pos, long, short]

        for i in range(1, n):
            for t in range(1, k + 1):
                no_pos = max(
                    dp[i - 1][t][0],
                    dp[i - 1][t][1] + prices[i],  # close long
                    dp[i - 1][t][2] - prices[i]  # close short
                )
                long = max(
                    dp[i - 1][t][1],
                    dp[i - 1][t - 1][0] - prices[i]  # open long
                )
                short = max(
                    dp[i - 1][t][2],
                    dp[i - 1][t - 1][0] + prices[i]  # open short
                )
                dp[i][t] = [no_pos, long, short]

        # Maximum profit at the last day with at most k transactions, no open positions
        return max(dp[n - 1][t][0] for t in range(k + 1))