from typing import List
from itertools import accumulate


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        without_mod = [p*s for p,s in zip(prices,strategy)]
        prefix_sum = list(accumulate(without_mod))

        ans = sum(without_mod)
        curr = 0
        for i in range(k//2, k):
            curr += prices[i]

        ans = max(ans, curr + prefix_sum[n - 1] - prefix_sum[k-1])
        for i in range(k, n):
            curr += prices[i]
            curr -= prices[i-k//2]
            ans = max(ans, curr + prefix_sum[i-k] + prefix_sum[n-1] - prefix_sum[i])

        return ans
