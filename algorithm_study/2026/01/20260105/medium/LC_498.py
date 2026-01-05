from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        ans = []
        for j in range(n + m - 1):
            dy = 1
            dx = -1
            x = j
            y = 0
            if j >= n:
                y = j - (n-1)
                x = n-1

            if j % 2 == 0:
                # reverse
                da = min(x, m-1-y)
                y, x = y+da, x-da
                dy *= -1
                dx *= -1

            while 0 <= y < m and 0 <= x < n:
                ans.append(mat[y][x])
                y += dy
                x += dx

        return ans
