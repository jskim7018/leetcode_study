from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        n = len(nums)
        prev_cnt = 0
        curr_increase_cnt = 1

        ans = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                curr_increase_cnt += 1
            else:
                ans = max(ans, min(prev_cnt, curr_increase_cnt),
                          max(prev_cnt, curr_increase_cnt) // 2)
                prev_cnt = curr_increase_cnt
                curr_increase_cnt = 1
        return ans
