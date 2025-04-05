from typing import List
from functools import cache

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m = len(mat)
        n = len(mat[0])

        @cache
        def solve(row, curr_target) -> int:
            if row >= m:
                return 0

            ret = float('inf')
            if curr_target <= 0:
                ret = solve(row + 1, curr_target - min(mat[row])) + min(mat[row])
            else:
                for i in range(n):
                    solved = solve(row+1, curr_target - mat[row][i])
                    if abs((solved + mat[row][i]) - curr_target) < abs(ret-curr_target):
                        ret = solved + mat[row][i]

            return ret

        return abs(solve(0, target) - target)
