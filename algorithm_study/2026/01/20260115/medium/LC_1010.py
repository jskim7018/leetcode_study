from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rems = defaultdict(int)
        ans = 0
        for t in time:
            t_rem = t % 60
            need = (60 - t_rem) % 60
            ans += rems[need]
            rems[t_rem] += 1

        return ans
