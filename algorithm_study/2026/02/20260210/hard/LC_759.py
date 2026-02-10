from collections import defaultdict


# class Interval:
#     def __init__(self, start: int = None, end: int = None):
#         self.start = start
#         self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = defaultdict(int)
        for e_schedule in schedule:
            for interval in e_schedule:
                intervals[interval.start] = max(intervals[interval.start], interval.end)
        interval_arr = [[s,e] for s,e in intervals.items()]
        interval_arr.sort()

        n = len(interval_arr)
        ans = []
        last_e = interval_arr[0][1]
        for i in range(1, n):
            s, e = interval_arr[i]
            if last_e < s:
                ans.append(Interval(last_e, s))

            last_e = max(last_e, e)

        return ans
