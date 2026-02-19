from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # 대각선으로 2점을 고른다.
        # 나머지 2점은 확정되고 그 점이 있는지만 확인한다. 있다면, x거리차, y거리차로 area를 구한다.

        points_dict = set(map(tuple, points))
        n = len(points)

        ans = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                p1 = points[i]
                p2 = points[j]

                p3 = (p1[0], p2[1])
                p4 = (p2[0], p1[1])

                if p3 in points_dict and p4 in points_dict:
                    area = abs(p1[0]-p2[0]) * abs(p1[1]-p2[1])
                    if area != 0:
                        ans = min(ans, area)

        if ans == float('inf'):
            return 0
        else:
            return ans
