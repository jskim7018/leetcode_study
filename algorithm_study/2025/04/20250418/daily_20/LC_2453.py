from typing import List
from collections import defaultdict


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mp = defaultdict(int)

        for num in nums:
            mp[num % space] += 1

        curr_max = 0
        ans = float('inf')
        for num in nums:
            if curr_max < mp[num % space]:
                ans = num
                curr_max = mp[num % space]
            elif curr_max == mp[num%space]:
                ans = min(ans, num)

        return ans
