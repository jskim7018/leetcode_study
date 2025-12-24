from typing import List
import heapq, math


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)

        while k:
            if heap[0] == 1:
                break

            biggest_pile = -heapq.heappop(heap)
            biggest_pile -= math.floor(biggest_pile/2)
            heapq.heappush(heap, -biggest_pile)
            k -= 1

        return sum([-h for h in heap])
