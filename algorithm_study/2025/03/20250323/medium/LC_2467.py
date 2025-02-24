from typing import List
from collections import deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = [[] for _ in range(len(amount))]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        visited = [False] * len(amount)

        bob_path = []
        def dfs(curr, graph, visited, path):
            nonlocal bob_path

            if visited[curr]:
                return
            visited[curr] = True
            path.append(curr)
            if curr == 0:
                bob_path = list(path)
                return

            for next in graph[curr]:
                dfs(next, graph,visited,path)

            path.pop()

        dfs(bob, graph,visited,[])

        visited = [False] * len(amount)
        ans = float('-inf')
        def dfs2(curr, time, amount_, graph, visited):
            nonlocal bob_path
            nonlocal ans

            if visited[curr]:
                return
            visited[curr] = True

            amount_ += amount[curr]
            if time < len(bob_path) and bob_path[time] == curr:
                amount_ -= amount[curr]//2
            if time < len(bob_path):
                tmp = amount[bob_path[time]]
                amount[bob_path[time]] = 0
            is_leaf = True
            for next in graph[curr]:
                if not visited[next]:
                    is_leaf = False
                    dfs2(next, time+1, amount_, graph, visited)
            if time < len(bob_path):
                amount[bob_path[time]] = tmp
            if is_leaf:
                ans = max(ans, amount_)

        dfs2(0, 0, 0, graph, visited)

        return ans
