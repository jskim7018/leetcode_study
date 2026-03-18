from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        n = len(points)

        ans = 0

        left_most = points[0][0]
        for i in range(1, n):
            x = points[i][0]

            if x - left_most > w:
                ans += 1
                left_most = x
        ans += 1

        return ans
