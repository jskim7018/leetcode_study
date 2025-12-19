from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] == nums[-1]:
            return 0
        else:
            return 1
