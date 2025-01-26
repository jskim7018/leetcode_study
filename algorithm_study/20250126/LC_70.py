from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def climb(i) -> int:
            if i == n:
                return 1
            if i > n:
                return 0

            ret = climb(i+1) + climb(i+2)
            return ret

        return climb(0)