from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_one_cnt = [0] * m
        col_one_cnt = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_one_cnt[i] += 1
                    col_one_cnt[j] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += (row_one_cnt[i]-1) * (col_one_cnt[j]-1)
        return ans
