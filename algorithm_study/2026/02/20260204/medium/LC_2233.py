from typing import List
from functools import reduce
import heapq


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        heap = list(nums)

        heapq.heapify(heap)

        while k:
            val = heapq.heappop(heap)
            heapq.heappush(heap, val+1)
            k -= 1

        return reduce(lambda a, b: (a*b) % mod, heap ,1)
