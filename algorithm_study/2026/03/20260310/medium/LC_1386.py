from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # 가능한 곳은 3곳. 왼쪽, 가운데, 오른쪽. 업데이트 하면서 하면 됨.
        # 2~5에 없으면 왼쪽 가능, 6~9에 없으면 오른쪽 가능, 4~7에 없으면 가운데 가능.

        ans = n*2

        curr_possible = defaultdict(lambda: [1, 1, 1])

        for r_seat in reservedSeats:
            row, col = r_seat

            curr_cnt = 0
            if curr_possible[row][0] == 1 and curr_possible[row][2] == 1:
                curr_cnt = 2
            elif sum(curr_possible[row]) > 0:
                curr_cnt = 1

            if 2 <= col <= 5:
                curr_possible[row][0] = 0
            if 4 <= col <= 7:
                curr_possible[row][1] = 0
            if 6 <= col <= 9:
                curr_possible[row][2] = 0

            new_cnt = 0
            if curr_possible[row][0] == 1 and curr_possible[row][2] == 1:
                new_cnt = 2
            elif sum(curr_possible[row]) > 0:
                new_cnt = 1

            ans -= curr_cnt - new_cnt
        return ans
