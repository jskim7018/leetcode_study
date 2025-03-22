from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        minimDistance = [float('inf')] * n

        edge_dict = {}

        for a, b, c in edges:
            key = (a, b)
            if key not in edge_dict or c < edge_dict[key]:
                edge_dict[key] = c

        graph = [[] for _ in range(n)]

        for edge, val in edge_dict.items():
            graph[edge[0]].append([edge[1], val])

        marked_st = set(marked)
        ans = float('inf')
        def dijkstra(start: int):
            nonlocal ans
            heap = []
            heapq.heapify(heap)

            heapq.heappush(heap, (0, start))

            while heap:
                dist, v = heapq.heappop(heap)
                if minimDistance[v] == float('inf'):
                    minimDistance[v] = dist
                    if v in marked_st:
                        ans = min(ans, minimDistance[v])
                        marked_st.remove(v)
                        if not marked_st:
                            break
                for u, edge_v in graph[v]:
                    if minimDistance[u] == float('inf'):
                        heapq.heappush(heap, (dist+edge_v, u))

        dijkstra(s)
        if ans == float('inf'):
            return -1
        else:
            return ans
