from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for f in flights:
            graph[f[0]].append((f[1], f[2]))

        def dijkstra():
            heap = []

            visited = defaultdict(int)
            for v, w in graph[src]:
                heap.append((w, v, 1))
            heapq.heapify(heap)
            visited[src] = 0
            while heap:
                w, v, stops = heapq.heappop(heap)
                if v in visited:
                    if visited[v] <= stops:
                        continue
                visited[v] = stops
                if v == dst and stops-1 <= k:
                    return w
                if stops > k:
                    continue

                for u, nw in graph[v]:
                    heapq.heappush(heap, (w+nw, u, stops+1))
            return -1

        return dijkstra()
