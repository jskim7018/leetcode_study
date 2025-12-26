from typing import List
from sortedcontainers import SortedList
import heapq


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        min_sum = 0
        max_sum = 0
        min_heap = [(num, i) for i, num in enumerate(nums)]
        max_heap = [(-num, i) for i, num in enumerate(nums)]

        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        used_min_idxes = SortedList()
        used_max_idxes = SortedList()

        while min_heap and max_heap:
            curr = heapq.heappop(min_heap)
            curr_min = curr[0]
            curr_min_idx = curr[1]

            min_start = used_min_idxes.bisect_left(curr_min_idx)-1
            min_end = used_min_idxes.bisect_left(curr_min_idx)
            l = 0
            r = n
            if min_start >= 0:
                l = used_min_idxes[min_start] + 1
            if min_end < len(used_min_idxes):
                r = used_min_idxes[min_end]
            left_min_cnt = curr_min_idx - l + 1
            right_min_cnt = r - curr_min_idx

            min_sum += curr_min * (left_min_cnt * right_min_cnt)

            curr = heapq.heappop(max_heap)
            curr_max = -curr[0]
            curr_max_idx = curr[1]

            max_start = used_max_idxes.bisect_left(curr_max_idx) - 1
            max_end = used_max_idxes.bisect_left(curr_max_idx)

            l = 0
            r = n
            if max_start >= 0:
                l = used_max_idxes[max_start] + 1
            if max_end < len(used_max_idxes):
                r = used_max_idxes[max_end]

            left_max_cnt = curr_max_idx - l + 1
            right_max_cnt = r - curr_max_idx

            max_sum += curr_max * (left_max_cnt * right_max_cnt)
            used_min_idxes.add(curr_min_idx)
            used_max_idxes.add(curr_max_idx)

        return max_sum - min_sum
