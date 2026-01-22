from itertools import accumulate
from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        grid_prefix_sum = []

        for i in range(m):
            grid_prefix_sum.append(list(accumulate(grid[i])))

        ans = 0
        for j in range(n):
            _sum = 0
            for i in range(m):
                _sum += grid_prefix_sum[i][j]
                if _sum <= k:
                    ans += 1
                else:
                    break
        return ans
