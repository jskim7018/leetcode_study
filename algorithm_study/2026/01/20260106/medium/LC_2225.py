from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        p_matches_lost = defaultdict(int)

        for m in matches:
            p_matches_lost[m[1]] += 1
            if m[0] not in p_matches_lost:
                p_matches_lost[m[0]] = 0

        ans = [[] for _ in range(2)]

        for k, v in p_matches_lost.items():
            if v == 0:
                ans[0].append(k)
            elif v == 1:
                ans[1].append(k)

        for i in range(2):
            ans[i].sort()

        return ans
