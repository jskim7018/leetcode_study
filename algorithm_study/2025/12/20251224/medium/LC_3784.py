from typing import List
from collections import defaultdict


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cost_mp = defaultdict(lambda: 0)

        total = 0
        for i, ch in enumerate(s):
            cost_mp[ch] += cost[i]
            total += cost[i]

        return total - max(cost_mp.values())
