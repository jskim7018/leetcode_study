from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:

        @lru_cache()
        def calcCost(i, prev_color, last_color) -> int:
            if i >= n//2:
                return 0

            ret = float('inf')

            for x in range(3):
                for a in range(3):
                    if x != prev_color and x != a and a != last_color:
                        ret = min(ret, cost[i][x] + cost[n-i-1][a] + calcCost(i+1, x, a))
            return ret

        return calcCost(0, -1, -1)
