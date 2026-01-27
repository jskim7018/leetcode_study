from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]*2))

        def dijkstra() -> int:
            heap = []
            dist = [float('inf')] * n
            dist[0] = 0
            heap.append((0, 0))
            while heap:
                w, u = heapq.heappop(heap)
                if u == n-1:
                    return int(dist[u])

                for v, _w in graph[u]:
                    if dist[u] + _w < dist[v]:
                        dist[v] = dist[u] + _w # TODO: memory 안터질려면 이렇게 해야함. 미리 dist 세팅.
                        heapq.heappush(heap, (dist[u] + _w, v))
            return -1

        return dijkstra()
