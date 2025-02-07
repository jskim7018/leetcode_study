from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_times = []

        next_start_time = 0

        for c in customers:
            wait_times.append(max(0,next_start_time-c[0])+c[1])
            if next_start_time <= c[0]:
                next_start_time = c[0]+ c[1]
            else:
                next_start_time += c[1]

        return sum(wait_times)/len(wait_times)
