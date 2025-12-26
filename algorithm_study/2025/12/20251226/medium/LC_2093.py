from typing import List
import heapq


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = [[] for _ in range(n)]
        for h in highways:
            graph[h[0]].append((h[1], h[2]))
            graph[h[1]].append((h[0], h[2]))

        def dijkstra(start: int):
            ans = float('inf')

            heap = []
            heapq.heappush(heap, (0, start, discounts))
            visited = dict()
            while heap:
                curr = heapq.heappop(heap)
                c_cost = curr[0]
                c_v = curr[1]
                c_discounts = curr[2]

                if c_v in visited and visited[c_v] >= c_discounts:
                    continue
                if c_v == n-1:
                    ans = min(ans, c_cost)

                visited[c_v] = c_discounts

                for u,w in graph[c_v]:
                    heapq.heappush(heap, (c_cost + w, u, c_discounts))
                    if c_discounts > 0:
                        heapq.heappush(heap, (c_cost + w//2, u, c_discounts-1))
            return ans

        ans = dijkstra(0)
        if ans == float('inf'):
            return -1
        else:
            return ans
