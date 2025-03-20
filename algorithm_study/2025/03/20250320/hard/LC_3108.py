from typing import List
from collections import defaultdict


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        available_nodes = set()
        union_find = UnionFind(n)
        for e in edges:
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]))
            available_nodes.add(e[0])
            available_nodes.add(e[1])
            union_find.union(e[0], e[1])

        ans = defaultdict(lambda: 2**30-1)
        for e in edges:
            ans[union_find.find(e[0])] &= e[2]

        q_ans = []

        for q in query:
            if union_find.find(q[0]) == union_find.find(q[1]):
                q_ans.append(ans[union_find.find(q[0])])
            else:
                q_ans.append(-1)

        return q_ans


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX  # Attach one root to another
            return True
        return False