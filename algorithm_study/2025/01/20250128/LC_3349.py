from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        def is_strict_incr(nums: List[int]) -> bool:
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    return False
            return True

        for i in range(len(nums) - k*2+1):
            if is_strict_incr(nums[i:i + k]) and is_strict_incr(nums[i+k:i+k+k]):
                return True

        return False
