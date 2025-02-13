from typing import List
from functools import cache


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(idx) -> int:
            if idx >= n:
                return 0

            ret = 0
            for i in range(idx + 1, n):
                ret = max(ret, dp(i) + (i-idx)*nums[i])

            return ret

        return dp(0)
