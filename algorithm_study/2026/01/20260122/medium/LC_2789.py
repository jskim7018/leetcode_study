from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)

        curr = nums[-1]

        ans = curr
        for i in range(n-2, -1, -1):
            if nums[i] <= curr:
                curr += nums[i]
            else:
                curr = nums[i]
            ans = max(ans, curr)

        return ans
