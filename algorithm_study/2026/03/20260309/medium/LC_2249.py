from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        # 그냥 가능한 점을 모두 해봄. 300 * 300 * 200
        # 하지만 더 효율적인게 있을까?
        # TODO: 각 circle 별로 하는게 더 효율적. 어차피 모든 점을 미리 구하고 해도 circle를 모두 체크 해야 하기 때문.
        def euclidean_distance(coord1: tuple, coord2: tuple) -> float:
            return ((coord1[0]-coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

        min_x, max_x = float('inf'), float('-inf')
        min_y, max_y = float('inf'), float('-inf')
        max_r = float('-inf')

        for c in circles:
            x, y, r = c
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            max_r = max(max_r, r)

        min_x = min_x - max_r
        max_x = max_x + max_r
        min_y = min_y - max_r
        max_y = max_y + max_r

        ans = 0
        for i in range(min_y, max_y + 1):
            for j in range(min_x, max_x + 1):
                for x,y,r in circles:
                    dist = euclidean_distance((y,x), (i,j))
                    if dist <= r:
                        ans += 1
                        break

        return ans
