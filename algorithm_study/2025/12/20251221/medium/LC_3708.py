from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_len = 2

        maxim = curr_len
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] + nums[i-2]:
                curr_len += 1
            else:
                curr_len = 2
            maxim = max(maxim, curr_len)

        return maxim
