from typing import List
from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # if cycle exists then return -1
        # can know if cycle exists if no node with in_degree 0 even when not processed.

        # bfs, kahn's algorithm 사용. 순서 저장 및 max 찾기
        graph = defaultdict(list)
        in_degrees = [0] * (n+1)
        for r in relations:
            graph[r[0]].append(r[1])
            in_degrees[r[1]] += 1

        def kahn() -> int:
            maxim = 0
            q = deque()
            for node in range(1, n+1):
                if in_degrees[node] == 0:
                    q.append((node, 1))

            while q:
                v, sem = q.popleft()
                maxim = max(maxim, sem)
                for u in graph[v]:
                    in_degrees[u] -= 1
                    if in_degrees[u] == 0:
                        q.append((u, sem + 1))
            for i in range(1, n+1):
                if in_degrees[i] != 0:
                    return -1

            return maxim

        return kahn()
