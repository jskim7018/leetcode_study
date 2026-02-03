from typing import List


class Solution:
    def finalElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(nums[0], nums[-1])
