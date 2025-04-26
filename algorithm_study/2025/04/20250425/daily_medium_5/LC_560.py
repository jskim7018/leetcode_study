from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        mp = defaultdict(int)
        mp[0] = 1
        curr_prefix = 0
        ans = 0
        for i in range(n):
            curr_prefix += nums[i]
            ans += mp[curr_prefix - k]
            mp[curr_prefix] += 1

        return ans
