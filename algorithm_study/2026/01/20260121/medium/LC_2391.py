from typing import List
from itertools import accumulate
from collections import defaultdict


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_travel = list(accumulate(travel))

        traveled = defaultdict(int)
        garbage_collected = defaultdict(int)
        n = len(garbage)

        garbage_types = ['M', 'G', 'P']
        for i in range(n):
            g = garbage[i]
            for gt in garbage_types:
                cnt = g.count(gt)
                garbage_collected[gt] += cnt
                if cnt != 0 and i-1 >= 0:
                    traveled[gt] = prefix_travel[i-1]

        ans = 0
        for gt in garbage_types:
            ans += traveled[gt]
            ans += garbage_collected[gt]

        return ans
