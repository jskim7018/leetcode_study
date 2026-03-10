from typing import List
from collections import defaultdict


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 동시에 미팅되고 있는 최대 값을 구해야 함.
        # 즉, 가장 많이 겹치는 구간의 갯수.
        # sweep line?
        sweep_line = defaultdict(int)
        for start, end in intervals:
            sweep_line[start] += 1
            sweep_line[end] -= 1

        sweep_line_list = list(sweep_line.items())
        sweep_line_list.sort()

        ans = 0
        curr_sweep_cnt = 0
        for _, cnt in sweep_line_list:
            curr_sweep_cnt += cnt
            ans = max(ans, curr_sweep_cnt)

        return ans
