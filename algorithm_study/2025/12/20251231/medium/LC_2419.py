from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxim = max(nums)

        cnt_maxim_consecutive = 0

        ans = 0
        for num in nums:
            if num == maxim:
                cnt_maxim_consecutive += 1
                ans = max(ans, cnt_maxim_consecutive)
            else:
                cnt_maxim_consecutive = 0

        return ans
