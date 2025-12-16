from functools import cache
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        @cache
        def dp(curr: int) -> int:
            nonlocal n
            nonlocal costs

            if curr == n:
                return 0

            ret = float('inf')
            for i in (1, 2, 3):
                next_step = curr + i
                if next_step <= n:
                    ret = min(ret, dp(next_step) +
                              costs[next_step-1] + (next_step-curr)**2)
            return ret

        return dp(0)
