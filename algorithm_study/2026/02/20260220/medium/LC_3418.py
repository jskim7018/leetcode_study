from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # dp[i][j][k]: max at i,j using k special ability
        m, n = len(coins), len(coins[0])

        # invalid path는 invalid하게 만드는 적절한 값을 사용해야함.
        # 예를 들면 단순히 0은 invalid로 볼 수 없음. (특히 음수가 존재할때)
        dp = [[float('-inf')] * 3 for _ in range(n)]
        dp[0][0] = coins[0][0]
        dp[0][1] = 0

        for j in range(n):
            for k in range(3):
                if j - 1 >= 0:
                    dp[j][k] = max(dp[j][k], dp[j - 1][k] + coins[0][j])
                    if k - 1 >= 0:
                        dp[j][k] = max(dp[j][k], dp[j - 1][k - 1])

        for i in range(1, m):
            new_dp = [[float('-inf')] * 3 for _ in range(n)]
            for j in range(n):
                for k in range(3):
                    if i - 1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], dp[j][k] + coins[i][j])
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k-1])
                    if j - 1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k] + coins[i][j])
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k-1])
            dp = new_dp

        return max(dp[n-1])
