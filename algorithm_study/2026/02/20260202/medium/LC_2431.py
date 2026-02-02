from typing import List


class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        n = len(price)
        dp = [[[0] * (maxCoupons+1) for _ in range((maxAmount+1))] for _ in range(n+1)]

        ans = 0

        if price[0] <= maxAmount:
            dp[0][price[0]][0] = max(dp[0][price[0]][0], tastiness[0])
            ans = max(ans, dp[0][price[0]][0])
            if price[0] // 2 <= maxAmount and maxCoupons >= 1:
                dp[0][price[0]//2][1] = max(dp[0][price[0]//2][1], tastiness[0])
                ans = max(ans, dp[0][price[0]//2][1])

        for i in range(1, n):
            for j in range(0, maxAmount+1):
                for k in range(0, maxCoupons+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j - price[i] >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - price[i]][k] + tastiness[i])
                    if j-price[i]//2 >= 0 and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - price[i]//2][k-1] + tastiness[i])
                    ans = max(ans, dp[i][j][k])

        return ans
