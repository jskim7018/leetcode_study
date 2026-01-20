from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9 + 7

        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])

        horizontalCuts.sort()
        verticalCuts.sort()

        h_max = 0
        v_max = 0

        for i in range(1, len(horizontalCuts)):
            h_max = max(h_max, horizontalCuts[i]-horizontalCuts[i-1])

        for i in range(1, len(verticalCuts)):
            v_max = max(v_max, verticalCuts[i] - verticalCuts[i - 1])

        return (h_max * v_max) % mod
