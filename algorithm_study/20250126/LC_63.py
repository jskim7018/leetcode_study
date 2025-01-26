from typing import List
from functools import cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @cache
        def dp(i, j) -> int:
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m-1 and j == n-1:
                return 1

            ret = dp(i+1, j) + dp(i, j+1)
            return ret

        return dp(0,0)
