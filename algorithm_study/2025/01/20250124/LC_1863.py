from typing import List


class Solution:
    total_sum = 0
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)

        self.add_xor_subsets(0,nums, 0)

        return self.total_sum

    def add_xor_subsets(self, idx: int, nums:List[int],
                        curr_xor: int):
        if idx >= len(nums):
            self.total_sum += curr_xor
            return

        self.add_xor_subsets(idx+1, nums, curr_xor ^ nums[idx])
        self.add_xor_subsets(idx+1, nums, curr_xor)
