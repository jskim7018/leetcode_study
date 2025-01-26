from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        events.insert(0, [0, 0])
        n = len(events)
        time = events[0][1]

        max_time = time
        for i in range(0, n-1):
            max_time = max(max_time, events[i+1][1] - events[i][1])

        min_index = float('inf')
        for i in range(0, n-1):
            time_diff = events[i+1][1] - events[i][1]

            if time_diff == max_time:
                min_index = min(min_index, events[i+1][0])

        return min_index
