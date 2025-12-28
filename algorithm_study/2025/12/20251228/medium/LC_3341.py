from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        def dijkstra(s_y: int, s_x: int) -> int:
            heap = [(0, s_y, s_x)]
            visited = [[False] * n for _ in range(m)]
            visited[s_y][s_x] = True
            dy = [-1,1,0,0]
            dx = [0,0, -1,1]

            while heap:
                move_time, cy, cx = heapq.heappop(heap)

                if cy == m-1 and cx == n-1:
                    return move_time

                for i in range(4):
                    ny = cy + dy[i]
                    nx = cx + dx[i]
                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        continue
                    if visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    heapq.heappush(heap, (max(move_time, moveTime[ny][nx])+1, ny, nx))

            return float('inf')

        return dijkstra(0, 0)
