from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []

        for interval in intervals:
            if not min_heap or min_heap[0] >= interval[0]:
                heapq.heappush(min_heap, interval[1])
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, interval[1])

        return len(min_heap)
