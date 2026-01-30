from typing import List
import heapq


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # health가 높은 순서로 이동한다.(일종의 health를 가중치로한 dijkstra)
        m, n = len(grid), len(grid[0])

        def dijkstra() -> bool:
            dy = [0,0,-1,1]
            dx = [1,-1,0,0]

            heap = [(-(health-grid[0][0]), 0, 0)]
            visited = [[0] * n for _ in range(m)]
            visited[0][0] = True

            while heap:
                curr_h, y, x = heapq.heappop(heap)
                curr_h = -curr_h

                if curr_h >= 1 and y == m-1 and x == n-1:
                    return True

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if ny < 0 or ny >= m or nx < 0 or nx >= n:
                        continue
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        if curr_h-grid[ny][nx] >= 1:
                            heapq.heappush(heap, (-(curr_h-grid[ny][nx]), ny, nx))
            return False

        return dijkstra()
