from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        ans = []
        for i in range(n-2):
            row_ans = []
            for j in range(n-2):
                maxim = 0
                for k in range(i, i+3):
                    maxim = max(maxim, max(grid[k][j:j+3]))
                row_ans.append(maxim)
            ans.append(row_ans)

        return ans
