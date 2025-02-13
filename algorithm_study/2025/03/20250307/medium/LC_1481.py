from typing import List
from collections import Counter
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        heap = []
        for c in counter.items():
            heap.append([c[1], c[0]])

        heapq.heapify(heap)

        for i in range(k):
            heap[0][0] -= 1
            if heap[0][0] == 0:
                heapq.heappop(heap)

        return len(heap)
