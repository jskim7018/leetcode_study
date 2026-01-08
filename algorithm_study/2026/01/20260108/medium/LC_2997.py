from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_xor = 0
        for num in nums:
            nums_xor ^= num

        nums_xor_bin = bin(nums_xor)[2:]
        k_bin = bin(k)[2:]

        max_width = max(len(nums_xor_bin), len(k_bin))
        nums_xor_bin = nums_xor_bin.zfill(max_width)
        k_bin = k_bin.zfill(max_width)

        ans = 0
        for a, b in zip(nums_xor_bin, k_bin):
            if a != b:
                ans += 1

        return ans
