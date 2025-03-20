from typing import List
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def solve(idx, can_buy) -> int:
            if idx >= n:
                return 0

            ret = 0
            if can_buy:
                ret = max(ret, solve(idx + 1, False) - prices[idx])
                ret = max(ret, solve(idx + 1, True))
            else:
                ret = max(ret, solve(idx + 2, True) + prices[idx])
                ret = max(ret, solve(idx + 1, False))

            return ret

        return solve(0, True)
