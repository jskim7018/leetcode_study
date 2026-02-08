from functools import cache


class Solution:
    def maxA(self, n: int) -> int:

        @cache
        def dp(n: int, copied: bool) -> int:
            if n <= 0:
                return 0
            if copied:
                return dp(n-2, False)
            else:
                ret = dp(n-1, False) + 1
                for i in range(1, n-1):
                    ret = max(ret, dp(n-i, True) * (i+1))
                return ret

        return dp(n, False)
