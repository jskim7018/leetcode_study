from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        ans = 0
        zero_cnt = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_cnt += 1

            while zero_cnt > 1:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1

            if r != l:
              ans = max(ans, r-l)

        return ans
