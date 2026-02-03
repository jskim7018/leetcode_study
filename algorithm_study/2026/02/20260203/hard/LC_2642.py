import heapq
from collections import defaultdict


class Graph:
    # dijkstra on-demand가 더 빠름. floyd warshall는 굳이긴 함. 사실 read가 addedge보다 훨씬 많으면 floyd가 나을수도.
    # with dynamic edges dijkstra wins over floyd warshall.
    # TODO: Can optimize even more by caching dijkstra results
    def __init__(self, n: int, edges):
        self.n = n
        self.graph = defaultdict(list)
        for u, v, w in edges:
            self.graph[u].append((v, w))
        self.cached_dists = defaultdict(list)

    def addEdge(self, edge):
        u, v, w = edge
        self.graph[u].append((v, w))
        self.cached_dists.clear()

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 in self.cached_dists:
            return self.cached_dists[node1][node2]

        dist = [float('inf')] * self.n
        dist[node1] = 0
        heap = [(0, node1)]

        while heap:
            cost, u = heapq.heappop(heap)

            if u == node2:
                return cost

            if cost > dist[u]:
                continue

            for v, w in self.graph[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(heap, (new_cost, v))

        return -1
