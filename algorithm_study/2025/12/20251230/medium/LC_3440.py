from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        events = [(s,e) for s,e in zip(startTime, endTime)]
        events.sort()
        n = len(startTime)
        suffix_max_free = [0] * n

        curr = eventTime
        for i in range(n):
            suffix_max_free[-i-1] = curr - events[-i-1][1]
            if i != 0:
                suffix_max_free[-i-1] = max(suffix_max_free[-i-1], suffix_max_free[-i])
            curr = events[-i-1][0]

        left_max = 0
        curr = 0
        ans = 0
        for i in range(n):

            right_max = 0
            s = 0
            e = eventTime
            if i - 1 >= 0:
                left_max = max(left_max, events[i-1][0] - curr)
                curr = events[i - 1][1]
                s = events[i-1][1]
            if i + 1 < n:
                right_max = suffix_max_free[i+1]
                e = events[i+1][0]
            if max(left_max, right_max) >= events[i][1] - events[i][0]:
                ans = max(ans, e-s)

            ans = max(ans, events[i][0] - s + e - events[i][1])

        return ans
