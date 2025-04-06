from typing import List
from functools import cache
import bisect


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        start_idxes = [v[0] for _, v in enumerate(offers)]

        @cache
        def solve(idx) -> int:
            if idx >= len(offers):
                return 0
            next_idx = bisect.bisect_left(start_idxes, offers[idx][1] + 1)
            ret = offers[idx][2]
            if next_idx < len(offers):
                ret += solve(next_idx)

            ret = max(ret, solve(idx + 1))

            return ret
        return solve(0)
