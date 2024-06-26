from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_cnt = 1

        cnt_inc = 1
        cnt_dec = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cnt_inc += 1
                cnt_dec = 1
            elif nums[i-1] > nums[i]:
                cnt_dec += 1
                cnt_inc = 1
            else:
                cnt_dec = 1
                cnt_inc = 1
            max_cnt = max(max_cnt, cnt_inc, cnt_dec)
        return max_cnt
