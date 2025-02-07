from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums[1:])
        ans = -1

        for i in range(len(nums)):
            if l_sum == r_sum:
                ans = i
                break
            l_sum += nums[i]
            if i+1 < len(nums):
                r_sum -= nums[i+1]

        return ans
