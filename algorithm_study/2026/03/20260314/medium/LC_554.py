from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        col_end_cnt = defaultdict(int)

        max_end_cnt = 0

        for row in wall:
            curr_col = 0
            for j in row[:-1]:
                curr_col += j
                col_end_cnt[curr_col] += 1
                max_end_cnt = max(max_end_cnt, col_end_cnt[curr_col])

        return n - max_end_cnt
