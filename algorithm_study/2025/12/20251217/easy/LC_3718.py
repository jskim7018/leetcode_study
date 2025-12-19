from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        _max = max(nums)

        rem = _max % k

        ans = _max + (k-rem)

        return ans