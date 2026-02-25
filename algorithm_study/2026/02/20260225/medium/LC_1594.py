from typing import List
import pytest


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7

        m, n = len(grid), len(grid[0])
        dp = [[[float('-inf')] * 2 for _ in range(n)] for _ in range(m)]
        if grid[0][0] >= 0:
            dp[0][0][1] = grid[0][0]
        else:
            dp[0][0][0] = -grid[0][0]

        ans = float('-inf')
        # 0 - neg, 1 - non-neg
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = 0
                if i - 1 >= 0:
                    if grid[i][j] >= 0:
                        dp[i][j][0] = max(dp[i][j][0], grid[i][j] * dp[i-1][j][0])
                        dp[i][j][1] = max(dp[i][j][1], grid[i][j] * dp[i-1][j][1])
                    else:
                        dp[i][j][0] = max(dp[i][j][0], -grid[i][j] * dp[i - 1][j][1])
                        dp[i][j][1] = max(dp[i][j][1], -grid[i][j] * dp[i - 1][j][0])
                if j - 1 >= 0:
                    if grid[i][j] >= 0:
                        dp[i][j][0] = max(dp[i][j][0], grid[i][j] * dp[i][j-1][0])
                        dp[i][j][1] = max(dp[i][j][1], grid[i][j] * dp[i][j-1][1])
                    else:
                        dp[i][j][0] = max(dp[i][j][0], -grid[i][j] * dp[i][j-1][1])
                        dp[i][j][1] = max(dp[i][j][1], -grid[i][j] * dp[i][j-1][0])

        ans = max(ans, dp[m-1][n-1][1] % mod)
        if ans == float('-inf'):
            return -1
        else:
            return ans


@pytest.mark.parametrize("input_grid, expected", [
    ([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]], -1),
    ([[1,-2,1],[1,-2,1],[3,-4,1]], 8),
    ([[1,3],[0,-4]], 0),
    ([[2,1,3,0,-3,3,-4,4,0,-4],[-4,-3,2,2,3,-3,1,-1,1,-2],[-2,0,-4,2,4,-3,-4,-1,3,4],[-1,0,1,0,-3,3,-2,-3,1,0],[0,-1,-2,0,-3,-4,0,3,-2,-2],[-4,-2,0,-1,0,-3,0,4,0,-3],[-3,-4,2,1,0,-4,2,-4,-1,-3],[3,-2,0,-4,1,0,1,-3,-1,-1],[3,-4,0,2,0,-2,2,-4,-2,4],[0,4,0,-3,-4,3,3,-1,-2,-2]],
     19215865)
])
def test_maxProductPath(input_grid, expected):
    sol = Solution()
    assert sol.maxProductPath(input_grid) == expected
