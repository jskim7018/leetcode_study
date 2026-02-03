from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        task_to_last_day = dict()

        curr_day = 1
        for t in tasks:
            if t in task_to_last_day:
                last_day = task_to_last_day[t]
                days_diff = curr_day - last_day
                curr_day += max(0, space-days_diff + 1)
            task_to_last_day[t] = curr_day
            curr_day += 1

        return curr_day - 1
