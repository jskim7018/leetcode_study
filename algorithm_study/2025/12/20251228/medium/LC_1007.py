from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        cand1 = tops[0]
        cand2 = bottoms[0]

        top_cand1 = 0
        top_cand2 = 0
        bottom_cand1 = 0
        bottom_cand2 = 0
        for i in range(n):
            if tops[i] != cand1 and bottoms[i] != cand1:
                top_cand1 = float('inf')
            else:
                if tops[i] != cand1:
                    top_cand1 += 1

            if tops[i] != cand2 and bottoms[i] != cand2:
                top_cand2 = float('inf')
            else:
                if tops[i] != cand2:
                    top_cand2 += 1

            if tops[i] != cand1 and bottoms[i] != cand1:
                bottom_cand1 = float('inf')
            else:
                if bottoms[i] != cand1:
                    bottom_cand1 += 1

            if tops[i] != cand2 and bottoms[i] != cand2:
                bottom_cand2 = float('inf')
            else:
                if bottoms[i] != cand2:
                    bottom_cand2 += 1
        ans = min(top_cand1, top_cand2, bottom_cand1, bottom_cand2)
        if ans == float('inf'):
            return -1
        else:
            return ans
