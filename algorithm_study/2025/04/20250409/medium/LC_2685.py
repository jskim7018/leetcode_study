from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False] * n

        def dfs(v: int):
            nonlocal edge_cnt
            nonlocal vertex_cnt
            if visited[v]:
                return
            visited[v] = True
            vertex_cnt += 1
            for u in graph[v]:
                edge_cnt += 1
                dfs(u)

        ans = 0
        for i in range(n):
            edge_cnt = 0
            vertex_cnt = 0
            dfs(i)
            edge_cnt //= 2

            if vertex_cnt > 0 and edge_cnt == (vertex_cnt*(vertex_cnt-1))//2:
               ans += 1

        return ans
