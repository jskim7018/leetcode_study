from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def calc_dist(x1: int, y1: int, x2: int, y2: int) -> float:
            return ((x1-x2)**2 + (y1-y2)**2)**0.5

        ans = []
        for q in queries:
            x2, y2, r = q

            # TODO: 아래 O(n) 코드를 improve 할 수 있나?
            points_in_cnt = 0
            for p in points:
                x1, y1 = p

                if calc_dist(x1, y1, x2, y2) <= r:
                    points_in_cnt += 1

            ans.append(points_in_cnt)

        return ans
