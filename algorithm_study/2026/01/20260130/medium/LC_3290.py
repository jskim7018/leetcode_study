from typing import List
from functools import cache


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        m = len(a)
        dp = [float('-inf')] * (m+1)
        # base case
        dp[0] = 0
        dp[1] = b[0] * a[0]

        # TODO: DP를 계속 optimize 해야 한다. 예: 2차원일때 이전값만 필요한지? 심지어 이전도 아니라 그냥 현재 1차원에서 더 작은 것만 필요한지 등등 고려해야한다.
        # TODO: 의존 관계를 파악해야 한다. 예를 들면 아래는 큰게 작은것에 의존하기에 큰것 부터 해야 한다.
        for i in range(1, n):
            for j in range(m, 0, -1):
                dp[j] = max(dp[j], dp[j-1] + a[j-1]*b[i])

        return int(dp[m])
