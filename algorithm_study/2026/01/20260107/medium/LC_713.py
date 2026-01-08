from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prod = 1
        l = 0

        ans = 0
        for r in range(n):
            prod *= nums[r]

            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1

            ans += r - l + 1

        return ans
