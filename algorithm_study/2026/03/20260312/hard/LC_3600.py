from typing import List
import heapq


class UnionFind:

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        elif self.rank[u] < self.rank[v]:
            self.parent[u] = v
        else:
            self.parent[v] = u
            self.rank[u] += 1

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Just do maximum spanning tree with must edges.
        # Then get top min k edges and upgrade, then get min.
        # Kruskal vs Prim? which would be the better choice for this problem?
        # => Kruskal because current focus is on edges.

        used_strength_min_heap = []
        union_find = UnionFind(n)

        max_edges_heap = []
        ans = float('inf')
        for u,v,s,must in edges:
            if must == 1:
                ans = min(ans, s)
                if union_find.find(u) == union_find.find(v):
                    return -1
                union_find.union(u, v)
            else:
                heapq.heappush(max_edges_heap, (-s, u, v))

        while max_edges_heap:
            s, u, v = heapq.heappop(max_edges_heap)
            s = -s
            if union_find.find(u) == union_find.find(v):
                continue

            union_find.union(u, v)

            heapq.heappush(used_strength_min_heap, s)

        for i in range(1, n):
            if union_find.find(i) != union_find.find(i-1):
                return -1

        while used_strength_min_heap and k:
            s = heapq.heappop(used_strength_min_heap)
            ans = min(ans, s*2)

            k -= 1

        if used_strength_min_heap:
            ans = min(ans, used_strength_min_heap[0])

        return ans
