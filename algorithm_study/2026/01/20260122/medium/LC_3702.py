from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        zeroes = 0
        total_xor = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            total_xor ^= num

        if total_xor != 0:
            return len(nums)
        elif zeroes == len(nums):
            return 0
        else:
            return len(nums) - 1
