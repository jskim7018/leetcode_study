from typing import List
import heapq


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        event_idx = 0
        heap = []
        day = 1
        ans = 0
        while event_idx < n or heap:
            while event_idx < n and events[event_idx][0] <= day:
                heapq.heappush(heap, events[event_idx][1])
                event_idx += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                ans += 1
            day += 1

        return ans
