from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        _min = min(nums)
        _max = max(nums)

        return (_max - _min) * k
