from typing import List
from collections import defaultdict
import math


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counter = defaultdict(lambda:0)

        for r in rectangles:
            w = r[0]
            h = r[1]
            _gcd = math.gcd(w,h)
            counter[(w//_gcd, h//_gcd)] += 1

        ans = 0
        for v in counter.values():
            ans += (v*(v-1))//2
        return ans
