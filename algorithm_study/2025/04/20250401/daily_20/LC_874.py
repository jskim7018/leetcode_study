from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_rows = defaultdict(SortedList)
        obstacles_cols = defaultdict(SortedList)

        ans = 0
        is_origin_obstacle = False
        for o in obstacles:
            x = o[0]
            y = o[1]
            if y == 0 and x == 0:
                is_origin_obstacle = True
            else:
                obstacles_rows[y].add(x)
                obstacles_cols[x].add(y)

        curr_dir = 0
        curr_y = 0
        curr_x = 0
        for c in commands:
            if c == -2:
                curr_dir = ((curr_dir-1)+4) % 4
            elif c == -1:
                curr_dir = (curr_dir+1) % 4
            else:
                if curr_dir == 0:
                    idx = obstacles_cols[curr_x].bisect_left(curr_y)
                    idx = idx
                    if idx >= len(obstacles_cols[curr_x]):
                        curr_y += c
                    else:
                        curr_y = min(curr_y+c, obstacles_cols[curr_x][idx]-1)
                elif curr_dir == 2:
                    idx = obstacles_cols[curr_x].bisect_left(curr_y)
                    idx = idx - 1
                    if idx == -1:
                        curr_y -= c
                    else:
                        curr_y = max(curr_y - c, obstacles_cols[curr_x][idx]+1)
                elif curr_dir == 1:
                    idx = obstacles_rows[curr_y].bisect_left(curr_x)
                    idx = idx
                    if idx >= len(obstacles_rows[curr_y]):
                        curr_x += c
                    else:
                        curr_x = min(curr_x + c, obstacles_rows[curr_y][idx]-1)
                else:
                    idx = obstacles_rows[curr_y].bisect_left(curr_x)
                    idx = idx - 1
                    if idx == -1:
                        curr_x -= c
                    else:
                        curr_x = max(curr_x - c, obstacles_rows[curr_y][idx]+1)
                if is_origin_obstacle:
                    obstacles_rows[0].add(0)
                    obstacles_cols[0].add(0)
                ans = max(ans, curr_y**2 + curr_x**2)

        return ans