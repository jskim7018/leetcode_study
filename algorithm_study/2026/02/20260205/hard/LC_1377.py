from typing import List
from collections import defaultdict, deque


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = defaultdict(list)

        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        prob = [0.0] * (n+1)
        visited = [False] * (n+1)

        def bfs():
            q = deque()

            q.append((1, 0))
            prob[1] = 1.0
            visited[1] = True

            while q:
                v, _t = q.popleft()
                if _t >= t:
                    break

                nxt_cnt = 0
                for u in tree[v]:
                    if not visited[u]:
                        nxt_cnt += 1

                for u in tree[v]:
                    if not visited[u]:
                        visited[u] = True
                        prob[u] = prob[v]/nxt_cnt
                        q.append((u, _t+1))
                if nxt_cnt > 0:
                    prob[v] = 0.0
            return prob[target]

        return bfs()
