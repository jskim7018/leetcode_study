from typing import List
from collections import defaultdict


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        """
        방법1: binary search. possible (have side length) range 0 ~ 10^9
        방법2: 0,0에서 거리별로 정렬. 가까운것 부터 처리. 같은 거리는 모두 처리하고 되는지 판정.
            거리는 max(abs(x), abs(y)) 같은 것 모두 처리 후 max length 가능.
        """
        dist_to_points = defaultdict(list)
        point_to_tag = dict()
        for i,(x, y) in enumerate(points):
            point_to_tag[(x,y)] = s[i]
            dist_to_points[max(abs(x), abs(y))].append((x,y))

        dist = list(dist_to_points.keys())
        dist.sort()
        points_cnt = 0
        tags_st = set()
        for d in dist:
            is_possible = True
            for p in dist_to_points[d]:
                tag = point_to_tag[p]
                if tag in tags_st:
                    is_possible = False
                    break
                else:
                    tags_st.add(tag)
            if is_possible:
                points_cnt += len(dist_to_points[d])
            else:
                break
        return points_cnt

