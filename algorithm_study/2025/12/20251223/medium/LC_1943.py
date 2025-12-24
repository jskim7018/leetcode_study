from typing import List
from collections import defaultdict


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(lambda:0)
        for s, e, mix in segments:
            mp[s] += mix
            mp[e] -= mix

        lst = [(t,mix) for t, mix in mp.items()]
        lst.sort()

        curr_mix = lst[0][1]
        bef_t = lst[0][0]
        ans = []

        for t, mix in lst[1:]:
            if curr_mix != 0:
                ans.append((bef_t, t, curr_mix))
            curr_mix = mix + curr_mix
            bef_t = t

        return ans
