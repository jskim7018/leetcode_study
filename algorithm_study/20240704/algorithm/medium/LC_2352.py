from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        set_ = set()
        for j in range(n):
            column = []
            for i in range(n):
                column.append(grid[i][j])
            set_.add(tuple(column))

        ans = 0
        for row in grid:
            if tuple(row) in set_:
                ans += 1

        return ans
