from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _max = max(nums)

        ans = 0
        for num in nums:
            ans += _max - num

        return ans
