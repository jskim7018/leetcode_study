from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        n = len(conversions) + 1

        graph = [[] for _ in range(n)]

        for c in conversions:
            graph[c[0]].append((c[1],c[2]))

        ans = [0] * n
        def dfs(v: int, curr_conv: int):
            ans[v] = curr_conv

            for nv, convFactor in graph[v]:
                dfs(nv, convFactor * curr_conv % mod)

        dfs(0, 1)

        return ans
