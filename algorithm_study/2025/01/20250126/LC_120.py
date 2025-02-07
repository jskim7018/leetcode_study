from typing import List
from functools import cache

class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)

        @cache
        def dp(i, j) -> int:
            if i == m-1:
                return triangle[i][j]

            ret = triangle[i][j] + min(dp(i+1, j), dp(i+1, j+1))

            return ret

        return dp(0, 0)
