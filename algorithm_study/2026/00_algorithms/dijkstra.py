import heapq
from typing import List, Tuple

def dijkstra(n: int, graph: List[List[Tuple[int, int]]], source: int) -> List[float]:
    """
    n      : number of nodes (0 to n-1)
    graph  : adjacency list
             graph[u] = [(v, weight), ...]
    source : starting node

    returns: list of shortest distances from source
    """

    dist = [float('inf')] * n
    dist[source] = 0

    heap = [(0, source)]  # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)

        # 🔑 Skip stale entries, TODO: Should not forget this or heap will explode
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist