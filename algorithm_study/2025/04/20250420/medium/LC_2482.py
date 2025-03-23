from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        rowOneCnt = [0] * m
        rowZeroCnt = [0] * m
        colOneCnt = [0] * n
        colZeroCnt = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    rowZeroCnt[i] += 1
                    colZeroCnt[j] += 1
                elif grid[i][j] == 1:
                    rowOneCnt[i] += 1
                    colOneCnt[j] += 1

        diff = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = rowOneCnt[i] + colOneCnt[j] - rowZeroCnt[i] - colZeroCnt[j]

        return diff
