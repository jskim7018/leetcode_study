from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for p in adjacentPairs:
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])

        start = 0
        for k, v in graph.items():
            if len(v) == 1:
                start = k

        ans = []
        def dfs(v: int, prev: int):
            ans.append(v)
            for u in graph[v]:
                if u != prev:
                    dfs(u, v)

        dfs(start, 10**6)

        return ans
