from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)

        # TODO: union-find 사용하면 더 깔끔하게 풀 수 있음.
        # TODO: 같은 parent를 가진다는 것은 이제 싸이클이 형성된다는 것이기에 해당 싸이클 edge가 마지막.
        e_to_idx = defaultdict(int)
        for i, e in enumerate(edges):
            e_to_idx[(e[1], e[0])] = i
            e_to_idx[(e[0], e[1])] = i
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = [False] * (n+1)

        stck = []
        def dfs(v: int, prev: int) -> set:
            visited[v] = True
            cycle_nodes = []
            for u in graph[v]:
                if u == prev:
                    continue
                if visited[u]:
                    while stck[-1] != u:
                        cycle_nodes.append(stck.pop())
                    cycle_nodes.append(u)
                    return cycle_nodes
                stck.append(u)
                cycle_nodes = dfs(u, v)
                if stck:
                    stck.pop()
                if len(cycle_nodes):
                    return cycle_nodes

            return cycle_nodes

        stck.append(1)
        cycle_nodes = dfs(1, 0)
        max_idx = 0
        for i in range(len(cycle_nodes)):
            max_idx = max(max_idx, e_to_idx[(cycle_nodes[i], cycle_nodes[(i+1)%len(cycle_nodes)])])

        return edges[max_idx]
