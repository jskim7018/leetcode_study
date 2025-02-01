from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_cols = set()
        zero_rows = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_cols.add(j)
                    zero_rows.add(i)

        for i in range(m):
            for j in range(n):
                if j in zero_cols or i in zero_rows:
                    matrix[i][j] = 0
