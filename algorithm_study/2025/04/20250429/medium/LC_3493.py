from typing import List


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        set_dict = dict()
        for i, property in enumerate(properties):
            set_dict[i] = set(property)

        graph = [[]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and len(set_dict[i].intersection(set_dict[j])) >= k:
                    graph[i].append(j)
        visited = [False]*n

        def dfs(v):
            if visited[v]:
                return
            visited[v] = True

            for nv in graph[v]:
                dfs(nv)

        ans = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1

        return ans
