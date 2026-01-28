from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for t in times:
            u, v, w = t
            graph[u].append((v, w))

        def dijkstra(start: int) -> int:
            min_dist = [float('inf')] * (n+1)

            min_dist[start] = 0

            heap = [(0, start)]

            while heap:
                dist, u = heapq.heappop(heap)

                for nxt in graph[u]:
                    nxt_v, nxt_w = nxt
                    if min_dist[nxt_v] > dist + nxt_w:
                        min_dist[nxt_v] = dist + nxt_w
                        heapq.heappush(heap, (dist+nxt_w, nxt_v))

            maxim = max(min_dist[1:])

            if maxim == float('inf'):
                return -1
            else:
                return maxim

        return dijkstra(k)
