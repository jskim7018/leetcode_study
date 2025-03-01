from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        tmp = [0] * n
        k = 0
        for j in range(n):
            if nums[j] != 0:
                tmp[k] = nums[j]
                k += 1
        nums = list(tmp)
        return nums
