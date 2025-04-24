from typing import List
from functools import lru_cache

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        st = set(nums)

        @lru_cache(maxsize=None)
        def solve(num: int) -> int:
            squared = num**2
            if squared not in st:
                return 0

            return solve(squared) + 1

        ans = 0
        for e in st:
            ans = max(ans, solve(e) + 1)
        if ans <= 1:
            return -1
        return ans
