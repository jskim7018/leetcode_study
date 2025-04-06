from typing import List
from math import perm


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = int(1e9+7)
        ranges.sort()
        cnt_groups = 1
        maxim_right = ranges[0][1]
        for i in range(1, len(ranges)):
            if maxim_right < ranges[i][0]:
                cnt_groups += 1
                maxim_right = ranges[i][1]
            else:
                maxim_right = max(maxim_right, ranges[i][1])

        ans = 2**cnt_groups
        ans %= MOD
        return ans