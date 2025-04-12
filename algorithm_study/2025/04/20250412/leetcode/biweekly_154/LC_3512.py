from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum_ = sum(nums)

        ans = sum_ % k

        return ans
