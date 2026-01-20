from typing import List
from collections import defaultdict


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        move_to_coord = defaultdict(tuple)

        for i in range(n):
            for j in range(n):
                move_to_coord[grid[i][j]] = (i, j)

        curr_move = 1
        curr_coord = move_to_coord[0]
        if curr_coord != (0,0):
            return False
        while curr_move in move_to_coord:
            nxt_coord = move_to_coord[curr_move]
            abs_dist_y = abs(curr_coord[0]-nxt_coord[0])
            abs_dist_x = abs(curr_coord[1]-nxt_coord[1])
            if ((abs_dist_x == 1 and abs_dist_y == 2) or
                    (abs_dist_x == 2 and abs_dist_y == 1)):
                curr_move += 1
                curr_coord = nxt_coord
            else:
                return False

        return True
