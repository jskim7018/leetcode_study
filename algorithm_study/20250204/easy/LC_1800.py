from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        sum = nums[0]
        ans = sum

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                sum += nums[i]
                ans = max(ans, sum)
            else:
                sum = nums[i]

        return ans
