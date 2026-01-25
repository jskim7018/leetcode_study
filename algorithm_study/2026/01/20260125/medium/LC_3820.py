from typing import List
from collections import defaultdict


class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        tree = defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        dists = defaultdict(list)

        # TODO: recursive DFS costs more than non recursive DFS or BFS.
        # TODO: Try not to use recursion as much as possible.
        def get_dists_from(v: int, dist:int):
            if visited[v]:
                return
            visited[v] = True
            dists[v].append(dist)

            for u in tree[v]:
                get_dists_from(u, dist + 1)

        for v in [x, y, z]:
            visited = [False] * n
            get_dists_from(v, 0)

        ans = 0
        for i in range(n):
            dists[i].sort()
            if dists[i][0] ** 2 + dists[i][1]**2 == dists[i][2] ** 2:
                ans += 1
        return ans
