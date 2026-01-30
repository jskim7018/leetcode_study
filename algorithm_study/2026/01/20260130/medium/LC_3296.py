from typing import List
import heapq


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # heap 사용시 쉽게 가능. O(n log n)
        # TODO: 좀 더 빠른 binary search 방식도 있다. 이것도 공부하자. 횟수 고정 후되는지 보기. 회수 binary search.
        heap = []
        for wt in workerTimes:
            heapq.heappush(heap, (wt, wt, 1))

        while mountainHeight > 1:
            curr_wt, original_wt, work_cnt = heapq.heappop(heap)
            mountainHeight -= 1
            work_cnt += 1
            heapq.heappush(heap, (curr_wt + original_wt*work_cnt, original_wt, work_cnt))
        return heap[0][0]
