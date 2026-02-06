from typing import List
from collections import defaultdict, deque


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 1. find number of graphs
        # 2. find number of unnecessary cables.
        # (since each just need to form a tree every cable more than node-1 is extra)

        graph = defaultdict(list)

        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])

        def bfs(v: int):
            nonlocal edges, nodes

            q = deque()
            q.append((v, v))  # curr, prev

            while q:
                curr, prev = q.popleft()

                for u in graph[curr]:
                    edges += 1
                    if not visited[u]:
                        nodes += 1
                        visited[u] = True
                        q.append((u, curr))


        extra_edges = 0
        graph_cnt = 0
        visited = [False] * n
        for i in range(n):
            edges = 0
            nodes = 1
            if not visited[i]:
                visited[i] = True
                graph_cnt += 1
                bfs(i)
                extra_edges += edges//2 - (nodes-1)
        if extra_edges >= graph_cnt-1:
            return graph_cnt-1
        else:
            return -1
