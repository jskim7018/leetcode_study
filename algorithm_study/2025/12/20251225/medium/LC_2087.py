from typing import List
import heapq


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int],
                rowCosts: List[int], colCosts: List[int]) -> int:

        s_y = startPos[0]
        s_x = startPos[1]

        h_y = homePos[0]
        h_x = homePos[1]

        ans = 0
        if s_y > h_y:
            for i in range(h_y, s_y):
                ans += rowCosts[i]
        else:
            for i in range(s_y + 1, h_y + 1):
                ans += rowCosts[i]
        if s_x > h_x:
            for i in range(h_x, s_x):
                ans += colCosts[i]
        else:
            for i in range(s_x + 1, h_x + 1):
                ans += colCosts[i]

        return ans
