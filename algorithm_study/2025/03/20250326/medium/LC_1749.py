from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxim = nums[0]
        minim = nums[0]

        ans = abs(nums[0])

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            ans = max(ans, abs(nums[i]))
            if nums[i] >= 0:
                ans = max(ans, abs(nums[i] - minim))
            elif nums[i] < 0:
                ans = max(ans, abs(nums[i] - maxim))
            maxim = max(maxim, nums[i])
            minim = min(minim, nums[i])

        return ans
