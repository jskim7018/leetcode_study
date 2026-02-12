from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # greedy 가능
        maxim = max(stones[1] - stones[0], stones[-1] - stones[-2])
        n = len(stones)
        for i in range(2, n):
            maxim = max(maxim, stones[i] - stones[i-2])

        return maxim
