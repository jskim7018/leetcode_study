from typing import List
import math


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        n = len(rungs)

        ans = 0

        curr = 0
        for i in range(0,n):
            diff = rungs[i] - curr
            if diff > dist:
                need = math.ceil(diff / dist)
                need -= 1
                ans += need
            curr = rungs[i]
        return ans
