class Solution:
    def cherryPickup(self, grid):

        m, n = len(grid), len(grid[0])

        # TODO: dp[r][c1][c2] -> 해당 r 도달햇을때  c1 c2 위치일때 최대.

        # dp[c1][c2] = max cherries from current row downward
        dp = [[-1] * n for _ in range(n)]
        dp[0][n-1] = grid[0][0] + grid[0][n-1]

        ans = 0
        # Process from bottom-1 to top
        for r in range(1, m):
            new_dp = [[-1] * n for _ in range(n)]

            for c1 in range(n):
                for c2 in range(n):

                    best = -1

                    # try all 9 transitions - 2명이 각각 3개의 가능한 이전 위치가 있기에 3*3 = 9개의 transition
                    for d1 in (-1, 0, 1):
                        for d2 in (-1, 0, 1):
                            nc1 = c1 + d1
                            nc2 = c2 + d2

                            if 0 <= nc1 < n and 0 <= nc2 < n:
                                if dp[nc1][nc2] != -1:
                                    best = max(best, dp[nc1][nc2])

                    # cherries at current row
                    if c1 == c2:
                        cherries = grid[r][c1]
                    else:
                        cherries = grid[r][c1] + grid[r][c2]
                    if best == -1:  # 이전 상태가 불가능이면 다음 상태도 불가능이기에 그렇게 설정.
                        new_dp[c1][c2] = -1
                    else:
                        new_dp[c1][c2] = cherries + best
                    ans = max(ans, new_dp[c1][c2])

            dp = new_dp

        return ans
