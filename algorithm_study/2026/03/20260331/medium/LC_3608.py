from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.count -= 1
        return True

    def component_size(self, x):
        return self.size[self.find(x)]

    def components(self):
        return self.count


class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        # Go backwards from when no edges are available.
        # Use union find to connect edges and check connected components count.
        edges.sort(key=lambda x: -x[2])

        union_find = UnionFind(n)
        ans_t = 0
        for u, v, t in edges:
            union_find.union(u, v)
            if union_find.components() < k:
                ans_t = t
                break

        return ans_t
