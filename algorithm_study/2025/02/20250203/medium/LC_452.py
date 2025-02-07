from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        ans = 1
        curr = points[0]
        for i in range(1, n):
            if curr[1] < points[i][0]:
                ans += 1
                curr = points[i]
            else:
                curr = (max(curr[0], points[i][0]), min(curr[1],points[i][1]))

        return ans
