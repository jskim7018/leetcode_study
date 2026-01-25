from typing import List
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        _total_sum = sum(nums)
        curr_sum = _total_sum
        half_total_sum = _total_sum/2.0

        heap = list([-num for num in nums])
        heapq.heapify(heap)

        ops = 0
        while curr_sum > half_total_sum:
            num = -heapq.heappop(heap)
            num /= 2.0
            curr_sum -= num
            heapq.heappush(heap, -num)
            ops += 1

        return ops
