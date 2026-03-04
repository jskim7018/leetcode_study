from typing import List
from collections import defaultdict


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_one_cnt = defaultdict(int)
        col_one_cnt = defaultdict(int)

        ones_pos = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_one_cnt[i] += 1
                    col_one_cnt[j] += 1
                    ones_pos.add((i,j))
        ans = 0
        for pos in ones_pos:
            if (row_one_cnt[pos[0]] == 1
                and col_one_cnt[pos[1]] == 1):
                ans += 1

        return ans
