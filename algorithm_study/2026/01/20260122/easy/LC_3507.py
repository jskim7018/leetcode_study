from typing import List
from itertools import pairwise


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:


        def check_non_decreasing(lst: List[int]) -> bool:
            n = len(lst)
            for i in range(1, n):
                if lst[i] < lst[i-1]:
                    return False
            return True

        ans = 0
        while not check_non_decreasing(nums):
            minim = float('inf')
            min_idx = -1
            for i, (a, b) in enumerate(pairwise(nums)):
                if a+b < minim:
                    minim = a+b
                    min_idx = i
            nums = nums[:min_idx] + [nums[min_idx] + nums[min_idx+1]] + nums[min_idx+2:]
            ans += 1

        return ans
