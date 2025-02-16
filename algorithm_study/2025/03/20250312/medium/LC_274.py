from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        minim = float("inf")

        ans = 0
        for i in range(len(citations)):
            minim = min(minim, citations[i])
            if minim >= i+1:
               ans = i+1
            else:
                break

        return ans
