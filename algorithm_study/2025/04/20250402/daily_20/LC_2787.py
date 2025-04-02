from functools import cache

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = int(1e9+7)

        @cache
        def solve(curr, num):
            if num == 0:
                return 1
            if curr**x > num:
                return 0

            ret = 0

            ret += solve(curr + 1, num - curr**x) + solve(curr + 1, num)
            ret %= MOD

            return ret

        ans = solve(1, n)

        solve.cache_clear()
        return ans
