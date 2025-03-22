from typing import List
from collections import Counter


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter()

        l = 0
        ans = 0
        sum_ = 0
        for r in range(n):
            counter[nums[r]] += 1
            sum_ += nums[r]
            while counter[nums[r]] > 1:
                counter[nums[l]] -= 1
                sum_ -= nums[l]
                l += 1
            ans = max(ans, sum_)

        return ans
