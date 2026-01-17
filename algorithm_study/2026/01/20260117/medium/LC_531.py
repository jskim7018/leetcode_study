from typing import List
from collections import defaultdict


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])

        row_b_cnt = defaultdict(int)
        col_b_cnt = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_b_cnt[i] += 1
                    col_b_cnt[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if row_b_cnt[i] == 1 and col_b_cnt[j] == 1:
                        ans += 1
        return ans
