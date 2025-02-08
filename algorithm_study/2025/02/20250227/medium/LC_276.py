from functools import cache


class Solution:
    def numWays(self, n: int, k: int) -> int:

        @cache
        def dp(idx, cnt) -> int:
            if idx >= n:
                return 1

            ret = 0

            ret += dp(idx+1, 2) * (k-1)
            ret += dp(idx+1, 1) * k

            return ret

        return dp(0, 0)
