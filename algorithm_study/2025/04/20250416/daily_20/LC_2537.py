from typing import List
from collections import defaultdict


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = defaultdict(int)
        curr_pair_cnt = 0
        ans = 0
        l = 0
        for r in range(n):
            counts[nums[r]] += 1
            curr_pair_cnt += counts[nums[r]] - 1
            while curr_pair_cnt >= k:
                ans += n-r
                counts[nums[l]] -= 1
                curr_pair_cnt -= counts[nums[l]]
                l += 1
        return ans
