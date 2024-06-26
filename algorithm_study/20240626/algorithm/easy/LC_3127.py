from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                tmp = grid[i][j]
                is_square = False
                grid[i][j] = 'W'
                is_square |= self.checkIfSquareExist(grid, 'W')
                grid[i][j] = 'B'
                is_square |= self.checkIfSquareExist(grid, 'B')
                grid[i][j] = tmp

                if is_square:
                    return is_square
        return False

    def checkIfSquareExist(self, grid: List[List[str]], c: str) -> bool:
        for i in range(0, 2):
            for j in range(0, 2):
                if grid[i][j] == grid[i+1][j] == grid[i][j+1] == grid[i+1][j+1] == c:
                    return True
        return False

"""
# ref: https://leetcode.com/problems/make-a-square-with-the-same-color/solutions/5080163/python-3-4-lines-countof-t-s-99-23/
# Mathematical way to do it
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        for i,j in product([0,1],[0,1]):
            square =(grid[i  ][j  ] + grid[i  ][j+1] +
                     grid[i+1][j  ] + grid[i+1][j+1])

            if countOf(square, "B") != 2: return True
            
        return False
"""