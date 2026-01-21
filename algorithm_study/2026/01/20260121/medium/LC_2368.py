from typing import List
from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted_st = set(restricted)
        tree = defaultdict(list)

        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        def dfs(v: int) -> int:
            if visited[v]:
                return 0
            visited[v] = True
            ret = 1
            for u in tree[v]:
                if u not in restricted_st:
                    ret += dfs(u)

            return ret
        visited = [False] * n

        return dfs(0)
