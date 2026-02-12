from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        to_add = nums[0]

        ans = 0
        for i in range(1, n):
            ans += to_add
            if nums[i] > to_add:
                to_add = nums[i]

        return ans
