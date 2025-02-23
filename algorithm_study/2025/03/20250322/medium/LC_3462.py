from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        arr = []
        for i in range(n):
            grid[i].sort(reverse=True)
            arr += grid[i][:limits[i]]

        arr.sort(reverse=True)

        return sum(arr[:k])
