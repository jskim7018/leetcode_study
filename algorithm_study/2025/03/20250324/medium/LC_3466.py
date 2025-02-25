from typing import List
from functools import cache

class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        n = len(lane1)
        lanes = [lane1, lane2]

        @cache
        def dp(idx, curr_lane, changed_cnt, init) -> int:
            nonlocal lanes

            if idx >= n:
                return 0

            ret = dp(idx+1, curr_lane, changed_cnt, False) + lanes[curr_lane][idx]

            if not init:
                ret = max(ret, 0)

            if changed_cnt < 2:
                ret = max(ret, dp(idx+1, curr_lane == 0, changed_cnt + 1, False) + lanes[curr_lane == 0][idx])
            return ret

        ans = float('-inf')
        for i in range(n):
            ans = max(ans, dp(i,0,0, True))

        return ans
