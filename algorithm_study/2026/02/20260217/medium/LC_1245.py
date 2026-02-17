from typing import List
from collections import defaultdict


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        tree = defaultdict(list)

        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        visited = set()

        ans = 0

        def dfs(v: int) -> int:
            nonlocal ans
            is_leaf = True

            children_depth = []
            for u in tree[v]:
                if u not in visited:
                    visited.add(u)
                    children_depth.append(dfs(u))
                    is_leaf = False

            if is_leaf:
                return 1
            else:
                children_depth.sort()
                if len(children_depth) == 1:
                    maxim_depth = children_depth[0]
                    ans = max(ans, maxim_depth)
                else:
                    ans = max(ans, children_depth[-1] + children_depth[-2])
                    maxim_depth = max(children_depth[-1], children_depth[-2])
                return maxim_depth + 1

        visited.add(0)
        dfs(0)

        return ans
