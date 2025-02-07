from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        m = len(grid[0])

        ans = []
        for i in range(n):
            if i % 2 == 0:
                for j in range(0,m,2):
                    ans.append(grid[i][j])
            else:
                lst = []
                for j in range(1,m,2):
                    lst.append(grid[i][j])
                ans += reversed(lst)

        return ans
