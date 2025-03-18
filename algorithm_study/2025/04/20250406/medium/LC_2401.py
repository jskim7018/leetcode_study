from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        curr_bits = 0
        ans = 0
        for r in range(n):
            while curr_bits & nums[r] != 0:
                curr_bits ^= nums[l]
                l += 1

            curr_bits |= nums[r]
            ans = max(ans, r - l + 1)

        return ans
