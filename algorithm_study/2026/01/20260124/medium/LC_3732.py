from typing import List
import heapq


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap_max = []
        heap_min = []
        for num in nums:
            heapq.heappush(heap_min, -num)
            while len(heap_min) > 2:
                heapq.heappop(heap_min)

            heapq.heappush(heap_max, num)
            while len(heap_max) > 2:
                heapq.heappop(heap_max)

        return max(abs(heap_min[0] * heap_min[1] * 10 ** 5),
                  abs(heap_max[0] * heap_max[1] * 10 ** 5),
                  abs(heap_min[1] * heap_max[1] * 10 ** 5))
