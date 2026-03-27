from functools import cache


class Solution:
    def integerReplacement(self, n: int) -> int:

        @cache
        def dp(num: int) -> int:
            if num == 1:
                return 0

            if num % 2 == 0:
                ret = dp(num//2) + 1
            else:
                ret = min(dp(num+1)+1, dp(num-1) + 1)

            return ret

        return dp(n)
