from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        _sum = 0

        n = len(nums)
        ans = 0
        for i in range(n):
            _sum += nums[i]
            if _sum < 0:
                break
            elif _sum > 0:
                ans += 1

        return ans
