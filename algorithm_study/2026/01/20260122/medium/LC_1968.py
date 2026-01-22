from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        for i in range(1, n, 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]

        return nums
