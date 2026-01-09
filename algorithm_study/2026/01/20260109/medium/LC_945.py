from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        next_number = nums[0]
        ans = 0
        for num in nums:
            if num < next_number:
                ans += next_number - num
            else:
                next_number = num
            next_number += 1
        return ans
