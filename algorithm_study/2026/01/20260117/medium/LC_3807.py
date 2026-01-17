from typing import List
from collections import deque


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        graph = [[] for _ in range(n)]

        for e in edges:
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]))

        l = 1
        r = 10**9

        def bfs(v: int, cnt: int, threshold: int) -> bool:
            visited = [False] * n

            q = deque()

            q.append((v, cnt))
            visited[v] = True

            while q:
                curr, curr_cnt = q.popleft()

                for u, w in graph[curr]:
                    if w <= threshold:
                        if visited[u]:
                            continue
                        if u == n-1 and curr_cnt + 1 <= k:
                            return True
                        if curr_cnt + 1 <= k:
                            visited[u] = True
                            q.append((u, curr_cnt+1))
            return False

        ans = -1
        while l <= r:
            mid = (l+r)//2

            possible = bfs(0, 0, mid)

            if possible:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
