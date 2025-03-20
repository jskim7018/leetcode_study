from typing import List
from collections import defaultdict


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]))
        ans = defaultdict(lambda: (-1, set()))

        visited = defaultdict(bool)
        def dfs(curr_v, vertexes_list):
            nonlocal curr_and_val

            if visited[curr_v]:
                return
            vertexes_list.add(curr_v)
            visited[curr_v] = True

            for e, v in graph[curr_v]:
                dfs(e, vertexes_list)
                curr_and_val &= v

            return

        q_ans = []

        for q in query:
            if not visited[q[0]]:
                vertexes_list = set()
                curr_and_val = 2 ** 30 - 1
                dfs(q[0], vertexes_list)
                for v in vertexes_list:
                    ans[v] = (curr_and_val, vertexes_list)
            if q[1] in ans[q[0]][1]:
                q_ans.append(ans[q[0]][0])
            else:
                q_ans.append(-1)

        return q_ans
