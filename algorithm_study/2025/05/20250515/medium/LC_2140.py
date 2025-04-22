from typing import List
from functools import cache


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def solve(idx) -> int:
            if idx >= n:
                return 0

            return max(solve(idx+1), solve(idx+questions[idx][1] + 1) + questions[idx][0])
        ans = solve(0)
        solve.cache_clear()
        return ans
