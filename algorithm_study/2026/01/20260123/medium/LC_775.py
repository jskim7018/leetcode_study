from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)

        curr_max = -1
        for i in range(1, n):
            if nums[i] < curr_max and i > 1:
                return False
            curr_max = max(curr_max, nums[i-1])

        return True