from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        squares = [(bl, tr) for bl, tr in zip(bottomLeft, topRight)]

        n = len(squares)

        def largest_intersecting(sqr1, sqr2) -> int:
            x1_bot, y1_bot = sqr1[0]
            x1_top, y1_top = sqr1[1]

            x2_bot, y2_bot = sqr2[0]
            x2_top, y2_top = sqr2[1]

            is_sqr2_inside = y1_bot <= y2_top <= y1_top and x2_bot <= x1_top and x1_bot <= x2_top
            if is_sqr2_inside:
                ret = min(y2_top - max(y2_bot, y1_bot), (min(x1_top, x2_top) - max(x1_bot, x2_bot)))
            else:
                ret = 0
            return ret ** 2

        ans = 0
        for i in range(n):
            sqr1 = squares[i]
            for j in range(n):
                if i != j:
                    sqr2 = squares[j]
                    ans = max(ans, largest_intersecting(sqr1, sqr2))

        return ans
