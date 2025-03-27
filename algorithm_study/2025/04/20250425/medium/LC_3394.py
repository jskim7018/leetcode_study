from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_ranges = []
        y_ranges = []

        for rect in rectangles:
            x_ranges.append((rect[0], rect[2]))
            y_ranges.append((rect[1], rect[3]))

        x_ranges.sort(key=lambda a:(a[0],a[1]))
        y_ranges.sort(key=lambda a:(a[0],a[1]))

        def checkIfCutPossible(ranges: List[int]) -> bool:
            m = len(ranges)
            cuts = 0
            curr_left_range = ranges[0]
            for i in range(1,m):
                curr_range = ranges[i]

                if curr_left_range[1] <= curr_range[0]:
                    cuts += 1
                if curr_left_range[1] < curr_range[1]:
                    curr_left_range = curr_range

                if cuts >= 2:
                    return True

            return False

        return checkIfCutPossible(x_ranges) or checkIfCutPossible(y_ranges)
