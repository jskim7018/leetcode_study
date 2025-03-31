from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        y1 = 0
        y2 = m - 1

        for i in range(m):
            is_all_zero = True
            for j in range(n):
                if grid[i][j] == 1:
                    is_all_zero = False
                    break
            if not is_all_zero:
                y1 = i
                break

        for i in range(m - 1, -1, -1):
            is_all_zero = True
            for j in range(n):
                if grid[i][j] == 1:
                    is_all_zero = False
                    break
            if not is_all_zero:
                y2 = i
                break
        x1 = 0
        x2 = n-1

        for j in range(n):
            is_all_zero = True
            for i in range(m):
                if grid[i][j] == 1:
                    is_all_zero = False
                    break
            if not is_all_zero:
                x1 = j
                break

        for j in range(n-1,-1,-1):
            is_all_zero = True
            for i in range(m):
                if grid[i][j] == 1:
                    is_all_zero = False
                    break
            if not is_all_zero:
                x2 = j
                break

        return (y2-y1+1) * (x2-x1+1)