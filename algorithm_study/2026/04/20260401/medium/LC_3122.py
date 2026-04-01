from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # dp?
        # greedy는 안되나?
        m, n = len(grid), len(grid[0])

        col_counter = []

        for j in range(n):
            counter = defaultdict(int)
            for i in range(m):
                counter[grid[i][j]] += 1
            top_3_counter = list(sorted(counter.items(), key=lambda x: -x[1]))[:3]
            col_counter.append(top_3_counter)

        @cache
        def dp(idx: int, prev: int) -> int:
            if idx >= n:
                return 0

            ret = dp(idx + 1, -1) + m
            for num, cnt in col_counter[idx]:
                if num != prev:
                    ret = min(ret, dp(idx + 1, num) + m - cnt)

            return ret

        return dp(0, -1)
