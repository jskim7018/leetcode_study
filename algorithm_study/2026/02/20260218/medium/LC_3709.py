# 일단 Segment Tree, Fewnick Tree로 가능해 보임.
# prefix sum 만들어서도 가능. startTime으로 이진 탐색. (record가 순서대로 들어오기에 가능.)
import bisect


class ExamTracker:

    def __init__(self):
        self.prefix_sum = []
        self.idx_to_time = []

    def record(self, time: int, score: int) -> None:
        self.prefix_sum.append(score)
        if len(self.prefix_sum) >= 2 :
            self.prefix_sum[-1] += self.prefix_sum[-2]
        self.idx_to_time.append(time)

    def totalScore(self, startTime: int, endTime: int) -> int:
        s_idx = bisect.bisect_left(self.idx_to_time, startTime) - 1
        e_idx = bisect.bisect_right(self.idx_to_time, endTime) - 1
        ret = 0
        if e_idx >= 0:
            ret += self.prefix_sum[e_idx]
        if s_idx >= 0:
            ret -= self.prefix_sum[s_idx]
        return ret

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)