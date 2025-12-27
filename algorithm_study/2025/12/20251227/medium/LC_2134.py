from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones_cnt = nums.count(1)

        curr_zero_cnt = total_ones_cnt - sum(nums[:total_ones_cnt])

        ans = curr_zero_cnt
        for i in range(total_ones_cnt, n+total_ones_cnt-1):
            i = i % n
            if nums[(i-total_ones_cnt+n)%n] == 0:
                curr_zero_cnt -= 1
            if nums[i] == 0:
                curr_zero_cnt += 1
            ans = min(ans, curr_zero_cnt)
        return ans
