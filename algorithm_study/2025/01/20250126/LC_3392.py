from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        cnt = 0
        for i in range(0, n-2):
            if (nums[i] + nums[i+2]) == nums[i+1]/2:
                cnt += 1

        return cnt
