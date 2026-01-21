from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        i = 1

        ans = 0
        while i < len(weight):
            if weight[i-1] > weight[i]:
                ans += 1
                i += 1
            i += 1

        return ans
