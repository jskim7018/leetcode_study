from functools import cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7

        dy = [0, 0, -1, 1]
        dx = [1, -1, 0, 0]

        @cache
        def dp(y: int, x: int, moves: int) -> int:
            if y >= m or x >= n or y < 0 or x < 0:
                return 1
            if moves == 0:
                return 0

            ret = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                ret += dp(ny, nx, moves-1)
                ret %= mod

            return ret

        return dp(startRow, startColumn, maxMove)
