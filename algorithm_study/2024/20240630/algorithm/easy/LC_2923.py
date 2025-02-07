from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if sum(grid[i]) == len(grid[i])-1:
                return i

        return -1
