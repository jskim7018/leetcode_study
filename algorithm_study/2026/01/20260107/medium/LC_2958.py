from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        counter = defaultdict(int)
        l = 0
        ans = 0
        for r in range(n):
            counter[nums[r]] += 1
            while l <= r and counter[nums[r]] > k:
                counter[nums[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
