from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0

        for i in range(n//2-1, -1, -1):
            left = i*2+1
            right = i*2+2

            ans += abs(cost[left] - cost[right])
            cost[i] += max(cost[left], cost[right])

        return ans
