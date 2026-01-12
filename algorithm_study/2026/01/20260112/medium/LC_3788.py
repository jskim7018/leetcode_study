from typing import List
from itertools import accumulate


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sum = list(accumulate(nums))

        ans = float('-inf')
        minim = nums[-1]
        for i in range(n-2, -1, -1):
            ans = max(ans, prefix_sum[i]-minim)
            minim = min(minim, nums[i])

        return ans
