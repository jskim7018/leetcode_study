from typing import List
from collections import deque, defaultdict


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs로 모든 경우 해보기
        m, n = len(grid), len(grid[0])

        def bfs() -> int:
            dy = [1, -1, 0, 0]
            dx = [0, 0, 1, -1]

            q = deque()

            q.append(((0, 0), 0, 0))  # (y, x), used, moved
            coord_to_used = [[float('inf')] * n for _ in range(m)]
            coord_to_used[0][0] = 0
            while q:
                (y, x), used, moved = q.popleft()
                if y == m-1 and x == n-1:
                    return moved

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        continue
                    next_moved = moved + 1
                    next_used = used

                    if grid[ny][nx] == 1:
                        next_used += 1
                    if next_used > k:
                        continue
                    if coord_to_used[ny][nx] > next_used:
                        q.append(((ny, nx), next_used, next_moved))
                        coord_to_used[ny][nx] = next_used

            return -1

        return bfs()
