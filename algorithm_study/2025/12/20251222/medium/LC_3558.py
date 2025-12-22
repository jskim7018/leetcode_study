from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10**9+7

        n = len(edges) + 1
        tree = [[] for _ in range(n+1)]

        for v, w in edges:
            tree[v].append(w)
            tree[w].append(v)

        visited = set()

        def dfs_max_depth(curr: int, depth: int) -> int:
            nonlocal visited
            if curr in visited:
                return 0
            visited.add(curr)

            ret = depth
            for nv in tree[curr]:
                ret = max(ret, dfs_max_depth(nv, depth+1))

            return ret

        max_depth = dfs_max_depth(1, 0)

        ans = 1
        for i in range(1, max_depth):
            ans *= 2
            ans %= mod

        return ans
