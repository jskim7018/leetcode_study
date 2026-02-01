from typing import List
from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for r in roads:
            graph[r[0]].append((r[1], r[2]))
            graph[r[1]].append((r[0], r[2]))

        def dfs(v: int) -> int:
            if visited[v]:
                return float('inf')
            visited[v] = True
            ret = float('inf')

            for u, w in graph[v]:
                ret = min(ret, w, dfs(u))

            return ret
        visited = [False] * (n+1)

        return dfs(1)
