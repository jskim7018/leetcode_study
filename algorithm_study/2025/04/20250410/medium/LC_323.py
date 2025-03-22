from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False] * n

        def dfs(v: int):
            if visited[v]:
                return
            visited[v] = True
            for u in graph[v]:
                dfs(u)

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)

        return ans
