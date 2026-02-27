from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        # 단순 거리가 1이 아니라 시간에 따라서 뒤죽박죽이라서 dijkstra 방식의 bfs를 해야함.
        # 갈 수 있으면 바로 간다. 현재 시간이 start보다 작으면 start를 현재로 하고 간다.
        # 못가면 버린다 (time > end)
        # time complexity: O((n + m) log n => 모든 node(n) visit + edge(m) 사용. priority q => log n
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append((e[1], e[2], e[3]))

        def dijkstra() -> int:
            time_dists = [float('inf')] * n

            min_heap = [(0, 0)]

            while min_heap:
                curr_t, v = heapq.heappop(min_heap)
                if time_dists[v] < curr_t:
                     continue

                if v == n-1:
                    return curr_t

                for u, s, e in graph[v]:
                    next_time_dist = float('inf')
                    if s <= curr_t <= e:
                        next_time_dist = curr_t + 1
                    elif curr_t < s:
                        next_time_dist = s + 1
                    if time_dists[u] > next_time_dist:
                        time_dists[u] = next_time_dist
                        heapq.heappush(min_heap, (next_time_dist, u))

            return -1

        return dijkstra()
