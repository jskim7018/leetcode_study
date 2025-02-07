from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        l = -1
        r = -1

        ans = float('inf')
        curr_sum = 0
        while r < n:
            while r < n and curr_sum < target:
                r += 1
                if r < n:
                    curr_sum += nums[r]

            while l < r and curr_sum >= target:
                ans = min(ans, r-l)
                l += 1
                if l < n:
                    curr_sum -= nums[l]
        if ans == float('inf'):
            ans = 0
        return ans
