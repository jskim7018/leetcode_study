from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_dist = [((point[0]**2+abs(point[1]**2))**0.5, point) for point in points]

        points_dist.sort()

        ans = []

        for i in range(k):
            ans.append(points_dist[i][1])

        return ans
