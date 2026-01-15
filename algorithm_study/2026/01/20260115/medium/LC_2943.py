from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        max_h_consecutive = 1
        max_v_consecutive = 1

        curr_consecutive = 1

        for i in range(1, n):
            if hBars[i] - hBars[i-1] == 1:
                curr_consecutive += 1
                max_h_consecutive = max(max_h_consecutive, curr_consecutive)
            else:
                curr_consecutive = 1

        curr_consecutive = 1
        for i in range(1, n):
            if vBars[i] - vBars[i-1] == 1:
                curr_consecutive += 1
                max_v_consecutive = max(max_v_consecutive, curr_consecutive)
            else:
                curr_consecutive = 1

        return min(max_v_consecutive, max_h_consecutive)
