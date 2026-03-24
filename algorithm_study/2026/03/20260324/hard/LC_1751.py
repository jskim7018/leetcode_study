from typing import List
from functools import cache
import bisect


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # dp + binary search
        events = [tuple(e) for e in events]
        n = len(events)
        events.sort()

        @cache
        def dp(idx: int, used_k: int) -> int:
            if used_k >= k:
                return 0
            if idx >= n:
                return 0

            # 현재 것을 안 넣는다.
            ret = dp(idx+1, used_k)

            # 현재 것을 넣는다.
            curr_end = events[idx][1]
            next_idx = bisect.bisect_right(events, (curr_end, float('inf'), float('inf')))
            ret = max(ret, dp(next_idx, used_k + 1) + events[idx][2])

            return ret

        return dp(0, 0)
