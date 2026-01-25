from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = float('inf')
        for i in range(0, len(nums)):
            if k - 1 + i < len(nums):
                ans = min(ans, nums[k-1+i] - nums[i])

        return ans
