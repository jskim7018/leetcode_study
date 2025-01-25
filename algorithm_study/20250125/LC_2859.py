from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        sum_ = 0

        for i, num in enumerate(nums):
            i_bin = bin(i)[2:]
            set_bits = i_bin.count('1')

            if set_bits == k:
                sum_ += num

        return sum_
