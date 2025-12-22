from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        y_x_list = [(y_e,x_e) for y_e, x_e in zip(y,x)]
        y_x_list.sort(reverse=True)

        chosen = set()

        ans = 0
        for y_e, x_e in y_x_list:
            if x_e not in chosen:
                ans += y_e
                chosen.add(x_e)
            if len(chosen) >= 3:
                break

        if len(chosen) < 3:
            return -1
        else:
            return ans
