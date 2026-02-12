from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        # dijkstra.
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]))

        def dijkstra() -> List[int]:
            dists = [float('inf')] * n
            dists[0] = 0

            heap = [(0, 0)]  # dist, v, time, disappear_time

            while heap:
                dist, v = heapq.heappop(heap)

                # TODO: invalidate heap edge that is no use anymore.
                if dist > dists[v]:
                    continue

                for u, w in graph[v]:
                    if dists[u] > dist + w and dist + w < disappear[u]:
                        dists[u] = dist + w
                        heapq.heappush(heap, (int(dists[u]), u))

            for i in range(len(dists)):
                if dists[i] == float('inf'):
                    dists[i] = -1

            return dists

        return dijkstra()
