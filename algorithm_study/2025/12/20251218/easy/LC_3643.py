from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(0, k//2):
            for j in range(0, k):
                grid[i+x][j+y], grid[x+k-i-1][j+y] \
                    = grid[x+k-i-1][j+y], grid[i+x][j+y]

        return grid
