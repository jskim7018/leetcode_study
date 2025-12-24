from typing import List
from functools import cache
import bisect


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()

        r_n = len(rides)

        @cache
        def dp(idx: int) -> int:
            if idx >= r_n:
                return 0

            ret = dp(idx+1)
            s = rides[idx][0]
            e = rides[idx][1]
            tip = rides[idx][2]

            next_idx = bisect.bisect_left(rides, e, key=lambda x:x[0])

            ret = max(ret, dp(next_idx) + tip + e-s)

            return ret

        return dp(0)
