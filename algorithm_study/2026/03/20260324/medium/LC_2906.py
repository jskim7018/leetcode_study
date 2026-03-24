from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # keep prefix mult, suffix mult
        # use to get each mult without the cell.
        mod = 12345
        m, n = len(grid), len(grid[0])

        prefix_mult = [[1] * n for _ in range(m)]
        suffix_mult = [[1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                prefix_mult[i][j] *= grid[i][j]
                if j - 1 >= 0:
                    prefix_mult[i][j] *= prefix_mult[i][j-1]
                prefix_mult[i][j] %= mod
                suffix_mult[i][n-j-1] *= grid[i][n-j-1]
                if n-j < n:
                    suffix_mult[i][n-j-1] *= suffix_mult[i][n-j]
                suffix_mult[i][n-j-1] %= mod

        prefix_v_total_mult = [1] * m
        suffix_v_total_mult = [1] * m

        for i in range(m):
            prefix_v_total_mult[i] *= prefix_mult[i][n-1]
            if i-1 >= 0:
                prefix_v_total_mult[i] *= prefix_v_total_mult[i-1]
            prefix_v_total_mult[i] %= mod

            suffix_v_total_mult[m-i-1] *= prefix_mult[m-i-1][n-1]
            if m-i < m:
                suffix_v_total_mult[m-i-1] *= suffix_v_total_mult[m-i]
            suffix_v_total_mult[m-i-1] %= mod

        ans = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j-1 >= 0:
                    ans[i][j] *= prefix_mult[i][j - 1]
                if j+1 < n:
                    ans[i][j] *= suffix_mult[i][j + 1]

                if i-1 >= 0:
                    ans[i][j] *= prefix_v_total_mult[i - 1]
                if i+1 < m:
                    ans[i][j] *= suffix_v_total_mult[i + 1]

                ans[i][j] %= mod

        return ans
