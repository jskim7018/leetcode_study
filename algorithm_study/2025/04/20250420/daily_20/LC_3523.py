from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0

        ans = 0
        for i in range(0, n):
            if nums[i] >= curr:
                ans += 1
                curr = nums[i]

        return ans
