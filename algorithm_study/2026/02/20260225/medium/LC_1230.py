from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        # dp[i][j] = probability of getting exactly j heads using the first i coins.
        # 각, i마다 넣거나 말거나 2가지 선택 있음.
        dp = [0.0] * (target+1)
        dp[0] = 1.0 - prob[0]
        if 1 < target+1:
            dp[1] = prob[0]

        for i in range(1, n):
            for j in range(target, -1, -1):
                dp[j] = dp[j] * (1-prob[i])
                if j-1 >= 0:
                    dp[j] += dp[j-1]*prob[i]

        return dp[target]
