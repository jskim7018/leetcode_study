from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minimCosts = []

        curr_minim = float('inf')

        for c in cost:
            curr_minim = min(curr_minim, c)
            minimCosts.append(curr_minim)

        return minimCosts
