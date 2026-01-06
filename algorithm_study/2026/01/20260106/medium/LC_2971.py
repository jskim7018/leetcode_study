from typing import List



class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        _sum = sum(nums)

        for num in nums:
            _sum -= num
            if num < _sum:
                return num + _sum
        return -1
