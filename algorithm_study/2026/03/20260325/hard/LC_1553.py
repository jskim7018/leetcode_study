from functools import cache


class Solution:
    def minDays(self, n: int) -> int:

        @cache
        def dp(curr_n: int) -> int:
            if curr_n == 0:
                return 0

            ret = float('inf')

            # try all possible div 2s
            if curr_n % 2 == 0:
                ret = dp(curr_n//2) + 1
            if (curr_n-1) % 2 == 0:
                ret = min(ret, dp((curr_n - 1) // 2) + 2)

            # try all possible div 3s
            if curr_n % 3 == 0:
                ret = min(ret, dp(curr_n//3) + 1)
            if (curr_n-1) % 3 == 0:
                ret = min(ret, dp((curr_n - 1) // 3) + 2)
            if (curr_n-2) % 3 == 0:
                ret = min(ret, dp((curr_n - 2) // 3) + 3)

            # try -1 only if clean div 2 and div 3 not possible.
            if curr_n % 2 != 0 and curr_n % 3 != 0:
                ret = dp(curr_n-1) + 1

            return ret

        return dp(n)
