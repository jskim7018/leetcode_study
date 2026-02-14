from typing import List
from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # 2가지. 0에서 시작해서 blue로 시작하는 것과 red로 시작하는 것 두가지 모두 해봄.
        # blue와 red 엣지 따로 heap에 저장해서 처리.

        graph = defaultdict(list)
        for re in redEdges:
            graph[re[0]].append((re[1], 0))
        for be in blueEdges:
            graph[be[0]].append((be[1], 1))

        # 0 - red, 1 - blue
        def alt_bfs() -> List[List[float]]:
            q = deque()

            q.append((0, 0, 0))
            q.append((0, 0, 1))
            dists = [[float("inf")] * 2 for _ in range(n)]
            while q:
                v, dist, need_color = q.popleft()

                if dist >= dists[v][need_color]:
                    continue
                dists[v][need_color] = dist

                for u, nxt_color in graph[v]:
                    if nxt_color == need_color:
                        q.append((u, dist+1, (need_color+1) % 2))
            return dists

        dists = alt_bfs()

        ans_dists = [-1] * n

        for i in range(n):
            ans_dists[i] = min(dists[i][0], dists[i][1])
            if ans_dists[i] == float('inf'):
                ans_dists[i] = -1

        return ans_dists
