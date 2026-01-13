from typing import List
from itertools import accumulate
import bisect
import math


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        squares.sort(key=lambda x: (x[1]+x[2]))
        squares_y = [s[1]+s[2] for s in squares]

        prefix_sum_squares = list(accumulate(l*l for _, _, l in squares))

        def comp_separate_squares(y: float) -> float:
            top, bottom = 0.0, 0.0
            idx = bisect.bisect_left(squares_y, math.ceil(y))
            r = n
            left = idx
            for i in range(idx, n):
                sqr = squares[i]
                bot_x, bot_y, l = sqr

                if y >= bot_y + l:
                    r = i
                    break

                top_y = bot_y + l

                if bot_y < y < top_y:
                    top_height = top_y - y
                    bottom_height = y - bot_y

                    top += top_height * l
                    bottom += bottom_height * l
                elif bot_y < y:
                    bottom += l*l
                else:
                    top += l*l
            if left-1 >= 0:
                bottom += prefix_sum_squares[left-1]
            if r < n and r-1 >= 0:
                top += prefix_sum_squares[n-1] - prefix_sum_squares[r-1]

            return top-bottom

        right = 1e9

        curr_y = 0
        to_change = right / 2
        comp = comp_separate_squares(curr_y)
        if comp < 0:
            to_change *= -1
        while True:
            while True:
                new_comp = comp_separate_squares(curr_y + to_change)

                if new_comp * comp > 0:
                    curr_y += to_change
                    break
                else:
                    to_change = to_change/2
            if abs(to_change) <= 1e-5:
                ans = curr_y
                break
        return ans
