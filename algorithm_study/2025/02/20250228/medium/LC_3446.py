from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        def sort_diag(y, x):
            arr = []
            tmp_y = y
            tmp_x = x
            while y < n and x < n:
                arr.append(grid[y][x])
                y += 1
                x += 1
            arr.sort(reverse=(tmp_x==0))
            idx = 0
            y = tmp_y
            x = tmp_x
            while y < n and x < n:
                grid[y][x] = arr[idx]
                idx += 1
                y += 1
                x += 1

        for i in range(n):
            sort_diag(i, 0)
        for j in range(1, n):
            sort_diag(0,j)

        return grid
