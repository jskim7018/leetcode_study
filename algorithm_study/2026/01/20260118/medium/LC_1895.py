from typing import List
from itertools import accumulate


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rows_pref_sum = [list(accumulate(grid[i])) for i in range(m)]
        cols_pref_sum = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            for i in range(m):
                cols_pref_sum[i][j] = grid[i][j]
                if i - 1 >= 0:
                    cols_pref_sum[i][j] += cols_pref_sum[i-1][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                k = 1
                diag_sum = 0
                while k + i - 1 < m and k + j - 1 < n:
                    is_possible = True
                    diag_sum += grid[i+k-1][j+k-1]
                    opp_diag_sum = 0
                    for l in range(k):
                        opp_diag_sum += grid[i+l][j+k-1-l]
                    if diag_sum != opp_diag_sum:
                        k += 1
                        continue
                    # rows
                    for l in range(i, i+k):
                        range_sum = rows_pref_sum[l][j+k-1]
                        if j - 1 >= 0:
                            range_sum -= rows_pref_sum[l][j-1]
                        if range_sum != diag_sum:
                            is_possible = False
                            break

                    if not is_possible:
                        k += 1
                        continue
                    # cols
                    for l in range(j, j+k):
                        range_sum = cols_pref_sum[i+k-1][l]
                        if i - 1 >= 0:
                            range_sum -= cols_pref_sum[i-1][l]
                        if range_sum != diag_sum:
                            is_possible = False
                            break

                    if is_possible:
                        ans = max(ans, k)
                    k += 1

        return ans
