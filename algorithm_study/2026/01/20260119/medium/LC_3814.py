from typing import List
from bisect import bisect_left
import heapq


class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)

        max_cap_per_cost = [[cost, [(cap, id)], id] for id, (cost,cap) in enumerate(zip(costs,capacity))]

        max_cap_per_cost.sort(key=lambda x: (x[0], -x[1][0][0]))

        for i in range(1, n):
            heap = max_cap_per_cost[i][1]
            heap.extend(max_cap_per_cost[i-1][1])
            heapq.heapify(heap)
            while len(heap) > 2:
                heapq.heappop(heap)
            heap.sort(reverse=True)

        ans = 0
        for i in range(n):
            cost = costs[i]
            cap = capacity[i]

            rem_budget = budget - cost

            idx = bisect_left(max_cap_per_cost, [rem_budget])
            idx -= 1
            if idx >= 0:
                candidate = max_cap_per_cost[idx]
                heap = max_cap_per_cost[idx][1]
                for j in range(len(heap)):
                    if heap[j][1] != i:
                        cap += heap[j][0]
                        rem_budget -= candidate[0]
                        break
            if rem_budget > 0:
                ans = max(ans, cap)
        return ans
