from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        row_to_col_idx = defaultdict(int)
        maxim = 0
        while True:
            is_possible = True
            for i in range(m):
                idx = bisect_left(mat[i], maxim)
                row_to_col_idx[i] = idx
                if row_to_col_idx[i] >= n:
                    return -1
                if mat[i][row_to_col_idx[i]] > maxim:
                    maxim = mat[i][row_to_col_idx[i]]
                    is_possible = False
                elif mat[i][row_to_col_idx[i]] < maxim:
                    row_to_col_idx[i] += 1
                    is_possible = False
            if is_possible:
                return maxim
