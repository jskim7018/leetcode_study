from typing import List
from collections import defaultdict


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        n = len(mat2[0])

        ans_mat = [[0] * n for _ in range(m)]

        mat1_row_dict = defaultdict(set)
        mat2_col_dict = defaultdict(set)

        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    mat1_row_dict[i].add(j)
        for j in range(n):
            for i in range(k):
                if mat2[i][j] != 0:
                    mat2_col_dict[j].add(i)

        for i in range(m):
            for j in range(n):
                for l in (mat1_row_dict[i] | mat2_col_dict[j]):
                    ans_mat[i][j] += mat1[i][l] * mat2[l][j]

        return ans_mat
