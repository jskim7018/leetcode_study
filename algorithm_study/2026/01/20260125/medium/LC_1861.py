from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        for i in range(m):
            stones = 0
            for j in range(n):
                if boxGrid[i][j] == '#':
                    stones += 1
                    boxGrid[i][j] = '.'
                if boxGrid[i][j] != '*' and j == n-1:
                    for k in range(stones):
                        boxGrid[i][j-k] = '#'
                    stones = 0
                elif boxGrid[i][j] == '*':
                    for k in range(stones):
                        boxGrid[i][j-1-k] = '#'
                    stones = 0

        rotated_grid = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_grid[j][i] = boxGrid[m-1-i][j]

        return rotated_grid
