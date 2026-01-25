from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr_right = float('-inf')

        remove = 0
        for interval in intervals:
            s, e = interval
            if s >= curr_right:
                curr_right = e
            else:
                curr_right = min(curr_right, e)
                remove += 1

        return remove
