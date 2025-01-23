from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        max_abs_diff = 0
        for i in range(len(nums)):
            # In python list[-1] is last element.
            max_abs_diff = max(max_abs_diff, abs(nums[i-1]-nums[i]))

        return max_abs_diff
