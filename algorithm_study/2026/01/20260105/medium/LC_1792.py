from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def ratio_incr_value(p: int, t: int):
            return (p+1)/(t+1)-(p/t)

        heap = []

        for c in classes:
            p = c[0]
            t = c[1]
            heap.append((-ratio_incr_value(p,t), p, t))

        heapq.heapify(heap)

        while extraStudents:
            r, p, t = heapq.heappop(heap)
            new_p, new_t = p + 1, t + 1
            new_r = ratio_incr_value(new_p, new_t)

            heapq.heappush(heap, (-new_r, new_p, new_t))

            extraStudents -= 1

        ans = 0
        for h in heap:
            p = h[1]
            t = h[2]
            ans += p/t
        return ans / len(heap)
