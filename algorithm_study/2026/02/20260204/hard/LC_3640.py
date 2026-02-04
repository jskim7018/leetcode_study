from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        curr_state = 0
        curr_total_sum = nums[0]

        curr_last_suffix_max = 0

        n = len(nums)
        ans = float('-inf')
        last_is_increase = False
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                last_is_increase = False
                if curr_state == 3:
                    ans = max(ans, curr_total_sum)
                curr_state = 0
                curr_total_sum = nums[i]
                curr_last_suffix_max = 0
            if nums[i - 1] < nums[i]:
                last_is_increase = True
                if curr_state == 0 or curr_state == 2:
                    curr_state += 1
                    curr_last_suffix_max += nums[i - 1]
                curr_total_sum += nums[i]
                if curr_state == 3:
                    ans = max(ans, curr_total_sum)
                curr_last_suffix_max = max(curr_last_suffix_max+nums[i], nums[i]+nums[i-1])
            elif nums[i - 1] > nums[i]:
                if curr_state == 0:
                    curr_total_sum = nums[i]
                    continue
                elif curr_state == 3:
                    ans = max(ans, curr_total_sum)
                if last_is_increase:
                    curr_total_sum = curr_last_suffix_max
                    curr_last_suffix_max = 0
                curr_state = 2
                curr_total_sum += nums[i]
                last_is_increase = False
        if curr_state == 3:
            ans = max(ans, curr_total_sum)

        return ans
