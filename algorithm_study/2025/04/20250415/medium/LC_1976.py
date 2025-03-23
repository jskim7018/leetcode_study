from typing import List
from collections import deque
import heapq
import pprint


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        MOD = 1e9+7

        for road in roads:
            graph[road[0]].append((road[1], road[2]))
            graph[road[1]].append((road[0], road[2]))

        time_cnt = [0] * n
        time_cnt[0] = 1
        min_time = [float('inf')] * n
        min_time[0] = 0
        overall_visited = [False] * n
        def bfs(v):
            q = list()
            q.append((0, v))
            heapq.heapify(q)
            while q:
                dist, vertex = heapq.heappop(q)
                if overall_visited[vertex]:
                    continue
                overall_visited[vertex] = True

                if vertex == n-1:
                    continue
                for u, t in graph[vertex]:
                    if min_time[u] > t+min_time[vertex]:
                        min_time[u] = t+min_time[vertex]
                        time_cnt[u] = time_cnt[vertex]
                    elif min_time[u] == t+min_time[vertex]:
                        time_cnt[u] += time_cnt[vertex]
                        time_cnt[u] %= MOD
                    else:
                        continue
                    heapq.heappush(q, (min_time[u], u))

        bfs(0)
        return int(time_cnt[n-1])
