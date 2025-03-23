from typing import List


# TODO: must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        maxim = 0
        for row in mat:
            maxim = max(maxim, max(row))

        for i in range(m):
            for j in range(n):
                if mat[i][j] == maxim:
                    return [i,j]

        return [-1,-1]
