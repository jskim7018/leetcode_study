from typing import List
from collections import defaultdict


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        tree = defaultdict(list)

        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        visited = [False] * n
        ans = 0
        def dfs(v: int) -> int:
            nonlocal ans
            visited[v] = True
            _sum = 1
            st = set()
            for u in tree[v]:
                if visited[u]:
                    continue
                sub_node_cnt = dfs(u)
                _sum += sub_node_cnt
                st.add(sub_node_cnt)
            if len(st) <= 1:
                ans += 1
            return _sum

        dfs(0)

        return ans
