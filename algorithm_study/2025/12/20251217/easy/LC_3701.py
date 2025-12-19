from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:

        sum = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                sum += num
            else:
                sum -= num
        return sum
