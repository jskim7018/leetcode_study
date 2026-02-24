from typing import List
import pytest


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        # dp[i][j] -> 현재 i에 있으면서 j day 사용했을때. O(n*k*n)

        dp = [[float('-inf')] * (k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0

        ans = 0
        for j in range(1, k + 1):  # k
            for i in range(n):  # n
                dp[i][j] = dp[i][j-1] + stayScore[j-1][i]
                for u in range(n):  # n
                    dp[i][j] = max(dp[i][j], dp[u][j-1] + travelScore[u][i])

                ans = max(ans, dp[i][j])

        return ans


@pytest.mark.parametrize("input_n, input_k, input_stayScore, input_travelScore, expected",[
    (2,1,[[2,3]], [[0,2],[1,0]], 3),
    (3,2,[[3,4,2],[2,1,2]], [[0,2,1],[2,0,4],[3,2,0]], 8),
    (2,1,[[1,1]],[[0,1],[6,0]], 6)
])
def test_maxScore(input_n, input_k, input_stayScore, input_travelScore, expected):
    sol = Solution()
    assert sol.maxScore(input_n, input_k, input_stayScore, input_travelScore) == expected
