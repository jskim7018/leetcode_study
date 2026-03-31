from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        prev_1st = nums[0] + nums[1]
        prev_2nd = nums[0] - nums[1]

        for i in range(2, n):
            curr_1st = max(prev_1st, prev_2nd) + nums[i]
            curr_2nd = prev_1st - nums[i]

            prev_1st = curr_1st
            prev_2nd = curr_2nd

        return max(prev_1st, prev_2nd)
