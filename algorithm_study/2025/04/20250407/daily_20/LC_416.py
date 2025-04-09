from typing import List
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        @cache
        def solve(idx, curr_sum) -> bool:
            if curr_sum == sum_ // 2:
                return True
            if idx >= n:
                return False
            if curr_sum > sum_ // 2:
                return False

            ret = solve(idx + 1, curr_sum) or solve(idx + 1, curr_sum + nums[idx])

            return ret

        return solve(0, 0)