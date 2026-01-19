from typing import List
from itertools import accumulate


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        rows_pref_sum = [list(accumulate(mat[i])) for i in range(m)]
        cols_pref_sum = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            for i in range(m):
                cols_pref_sum[i][j] = mat[i][j]
                if i - 1 >= 0:
                    cols_pref_sum[i][j] += cols_pref_sum[i - 1][j]

        max_k = 0
        for i in range(m):
            for j in range(n):
                k = 1
                _sum = 0
                # TODO: can be improved with 2d prefix sum and binary search
                while k + i - 1 < m and k + j - 1 < n:
                    _sum += rows_pref_sum[k+i-1][j + k - 1]
                    if j - 1 >= 0:
                        _sum -= rows_pref_sum[k+i-1][j - 1]

                    _sum += cols_pref_sum[k + i - 1][j + k - 1]
                    if i - 1 >= 0:
                        _sum -= cols_pref_sum[i - 1][j + k - 1]

                    _sum -= mat[k+i-1][j+k-1]
                    if _sum <= threshold:
                        max_k = max(max_k, k)
                    else:
                        break
                    k += 1

        return max_k
