from sortedcontainers import SortedDict


class MyCalendarTwo:

    def __init__(self):
        self.line_sweep = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.line_sweep.setdefault(startTime, 0)
        self.line_sweep.setdefault(endTime, 0)

        self.line_sweep[startTime] += 1
        self.line_sweep[endTime] -= 1

        curr = 0
        for pos, cnt in self.line_sweep.items():
            curr += cnt
            if curr > 2:
                self.line_sweep[startTime] -= 1
                self.line_sweep[endTime] += 1
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)