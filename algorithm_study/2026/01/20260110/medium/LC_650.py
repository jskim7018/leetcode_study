from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(_n: int, prev_copy: int) -> int:
            if _n < 0:
                return float('inf')
            elif _n == 0:
                return 0

            typed_cnt = n - _n
            ret = dp(_n-typed_cnt, typed_cnt) + 2
            if prev_copy != -1:
                ret = min(ret, dp(_n-prev_copy, prev_copy) + 1)

            return ret

        return dp(n-1, -1)
