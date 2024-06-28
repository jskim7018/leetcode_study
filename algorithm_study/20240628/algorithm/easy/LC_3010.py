from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums2 = nums[1:]
        nums2.sort()
        return nums[0] + sum(nums2[:2])
