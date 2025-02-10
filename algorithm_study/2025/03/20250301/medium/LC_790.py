from functools import cache


class Solution:

    def numTilings(self, n: int) -> int:
        mod = 1e9 + 7
        print(mod)
        @cache
        def dp(idx: int) -> int:
            if idx == n:
                return 1
            if idx > n:
                return 0

            ret = 0

            ret += dp(idx + 2) + dp(idx + 1)
            next = idx + 3
            while next <= n:
                ret += dp(next) * 2
                next += 1
            ret %= mod

            return int(ret)

        return dp(0)
