from typing import List
from itertools import accumulate


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # dp 같아 보이지만 prefix + greedy

        prefix_sum_top = list(accumulate(grid[0]))
        prefix_sum_bottom = list(accumulate(grid[1]))

        n = len(grid[0])
        ans = float('inf')
        for i in range(n):
            cand = 0
            if i - 1 >= 0:
                cand = max(cand, prefix_sum_bottom[i-1])
            if i + 1 < n:
                cand = max(cand, prefix_sum_top[n-1] - prefix_sum_top[i])
            ans = min(ans, cand)

        return ans