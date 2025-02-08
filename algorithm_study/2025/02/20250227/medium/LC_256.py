from typing import List
from functools import cache

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        @cache
        def dp(idx, befColor) -> int:
            if idx >= n:
                return 0

            ret = float('inf')
            for i in range(len(costs[idx])):
                if i != befColor:
                    ret = min(ret, dp(idx+1, i) + costs[idx][i])

            return ret

        return dp(0, -1)
