from typing import List


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        prev_prev = nums[0]
        prev = nums[1]

        if colors[0] != colors[1]:
            prev += prev_prev
        prev = max(prev, prev_prev)

        for i in range(2, n):
            curr = nums[i] + prev_prev
            if colors[i] != colors[i-1]:
                curr = max(curr, nums[i] + prev)
            prev_prev = prev
            prev = max(curr, prev)

        return prev
