from typing import List
from functools import cache
import bisect


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Every robot has only 1 bullet
        # dp + binary search
        # 한곳의 경우 몇개 잡을 수 있는지 binary search로 바로 알 수 있음.
        # 한 구간을 두 로봇에 동시에 쏠때 unique한 갯수를 구해야 함.
        # 이때는 안겹치는 곳에서 갯수를 구하면 됨.

        n = len(robots)

        rd = list(zip(robots, distance))
        rd.sort()
        walls.sort()

        def _count_between(left: int, right: int) -> int:
            return max(0, (bisect.bisect_right(walls, right) - 1) - (bisect.bisect_left(walls, left)) + 1)

        @cache
        def dp(idx: int, prev_dir: int) -> int:
            if idx >= n:
                return 0

            ret = 0
            left = rd[idx][0] - rd[idx][1]
            mid = rd[idx][0]
            right = rd[idx][0] + rd[idx][1]

            left_bound = -1
            right_bound = float('inf')
            if idx - 1 >= 0:
                left_bound = rd[idx-1][0] + 1
            if idx + 1 < n:
                right_bound = rd[idx+1][0] - 1

            if prev_dir == 1:
                left_bound = rd[idx-1][0] + rd[idx-1][1] + 1

            # left
            ret = max(ret, dp(idx + 1, 0) + _count_between(max(left, left_bound), mid))

            # right
            ret = max(ret, dp(idx + 1, 1) + _count_between(mid, min(right, right_bound)))

            return ret

        return dp(0, 0)
