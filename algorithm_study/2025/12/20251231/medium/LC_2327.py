from functools import cache


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7

        @cache
        def dp(day: int) -> int:
            if day > n:
                return 0
            ret = 0
            if day + forget > n:
                ret = 1

            for i in range(forget-delay):
                ret += dp(day + delay + i)

            ret %= mod
            return ret

        return dp(1)
