from typing import List
from functools import cache

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        @cache
        def dp(i, j) -> int:
            if i >= m or j >= n or i < 0 or j < 0:
                return 0
            if int(matrix[i][j]) == 0:
                return 0

            ret = int(matrix[i][j]) + min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))

            return ret


        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dp(i,j)**2)

        return ans
