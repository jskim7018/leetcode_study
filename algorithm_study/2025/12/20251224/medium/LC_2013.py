from typing import List
from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.coord_cnt_mp = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.coord_cnt_mp[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        cnt = 0

        available_coords = list(self.coord_cnt_mp.keys())
        for (_x, _y) in available_coords:
            if _y != y:
                continue
            if _x != x:
                side_len = abs(_x-x)
                top_y = y - side_len
                bot_y = y + side_len

                cnt += self.coord_cnt_mp[(_x, bot_y)] * self.coord_cnt_mp[(x, bot_y)] \
                    * self.coord_cnt_mp[(_x, y)]
                cnt += self.coord_cnt_mp[(_x, top_y)] * self.coord_cnt_mp[(x, top_y)] \
                    * self.coord_cnt_mp[(_x, y)]

        return cnt
