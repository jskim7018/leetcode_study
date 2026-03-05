from typing import List
from sortedcontainers import SortedSet


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ans = [[0] * (n-k+1) for _ in range(m-k+1)]
        for i in range(m-k+1):
            for j in range(n-k+1):
                sorted_set = SortedSet()

                for k1 in range(i, i+k):
                    for k2 in range(j, j+k):
                        sorted_set.add(grid[k1][k2])

                n_sl = len(sorted_set)
                min_diff = float('inf')
                for idx in range(1, n_sl):
                    min_diff = min(min_diff, sorted_set[idx] - sorted_set[idx-1])
                if min_diff != float('inf'):
                    ans[i][j] = min_diff

        return ans
