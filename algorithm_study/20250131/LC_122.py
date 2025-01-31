from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]

        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            else:
                ans += prices[i] - curr
                curr = prices[i]

        return ans
