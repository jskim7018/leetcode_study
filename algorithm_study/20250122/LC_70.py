from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def climb(n: int):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            return climb(n-1) + climb(n-2)

        return climb(n)
