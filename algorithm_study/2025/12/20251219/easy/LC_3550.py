from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            _sum = 0
            while num > 0:
                _sum += num % 10
                num //= 10
            if _sum == i:
                return i
        return -1
