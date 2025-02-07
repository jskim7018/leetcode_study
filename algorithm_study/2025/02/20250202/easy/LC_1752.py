from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot_idx = 0

        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                pivot_idx = i
                break

        new_nums = nums[pivot_idx:] + nums[:pivot_idx]
        print(new_nums)
        for i in range(1, len(new_nums)):
            if new_nums[i-1] > new_nums[i]:
                return False

        return True
