from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)

        n = len(nums)

        score = 0
        for i in range(n//2):
            score -= nums[i] ** 2

        for i in range(n//2, n):
            score += nums[i] ** 2

        return score
