from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])

        ans = []
        for i in range(m):
            for j in range(n):
                up = i - 1
                left = j - 1
                if land[i][j] == 1 and (up < 0 or land[up][j] == 0) and \
                    (left < 0 or land[i][left] == 0):
                    r2 = i
                    c2 = j
                    while r2 < m and land[r2][c2] != 0:
                        r2 += 1
                    while c2 < n and land[r2-1][c2] != 0:
                        c2 += 1
                    ans.append((i,j,r2-1,c2-1))
        return ans
