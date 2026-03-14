from typing import List
from collections import defaultdict


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # binary search 가능
        pairs.sort()

        n = len(pairs)
        best_val = defaultdict(int)
        ans = 0
        for i in range(n):
            s, e = pairs[i]
            best_prev_val = 0

            for j in range(i):
                _, prev_e = pairs[j]
                if prev_e < s:
                    best_prev_val = max(best_prev_val, best_val[prev_e])

            best_val[e] = max(best_val[e], best_prev_val + 1)
            ans = max(ans, best_val[e])

        return ans