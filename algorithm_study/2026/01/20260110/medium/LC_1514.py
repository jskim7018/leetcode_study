from typing import List
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = [[] for _ in range(n)]

        for i, e in enumerate(edges):
            graph[e[0]].append((e[1], succProb[i]))
            graph[e[1]].append((e[0], succProb[i]))

        def dijkstra() -> float:
            heap = []

            heapq.heappush(heap, (-1.0, start_node))
            visited = [False] * n
            while heap:
                prob, node = heapq.heappop(heap)
                prob = -prob
                visited[node] = True

                if node == end_node:
                    return prob

                for u, w in graph[node]:
                    if not visited[u]:
                        heapq.heappush(heap, (-(prob*w), u))
            return 0

        return dijkstra()
