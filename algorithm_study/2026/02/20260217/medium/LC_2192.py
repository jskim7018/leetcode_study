from typing import List
from collections import defaultdict, deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        in_degrees = [0] * n
        graph = defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            in_degrees[e[1]] += 1

        ans = [set() for _ in range(n)]

        def bfs():
            q = deque()
            for i in range(n):
                if in_degrees[i] == 0:
                    q.append(i)

            while q:
                v = q.popleft()

                for u in graph[v]:
                    in_degrees[u] -= 1
                    ans[u].update(ans[v])
                    ans[u].add(v)
                    if in_degrees[u] == 0:
                        q.append(u)

        bfs()
        for i in range(n):
            lst = list(ans[i])
            lst.sort()
            ans[i] = lst

        return ans
