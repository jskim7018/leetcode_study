from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)

        is_even = total % 2 == 0

        if is_even:
            return len(nums)-1
        else:
            return 0
