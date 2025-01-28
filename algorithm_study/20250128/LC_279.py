from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:
        sqr_list = []
        i = 1
        while i*i <= n:
            sqr_list.append(i*i)
            i += 1

        @cache
        def dp(n) -> int:
            if n < 0:
                return float('inf')
            if n == 0:
                return 0

            ret = float('inf')
            for sqr in sqr_list:
                if n-sqr >= 0:
                    ret = min(ret, dp(n-sqr)+1)
                else:
                    break
            return ret

        return dp(n)
