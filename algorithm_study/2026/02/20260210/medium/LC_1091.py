from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # simple bfs
        n = len(grid)

        def bfs() -> int:
            if grid[0][0] == 1:
                return -1

            dy = [1,1,-1,-1,0,0,1,-1]
            dx = [1,-1,1,-1,-1,1,0,0]
            visited = [[False] * n for _ in range(n)]
            q = deque()
            q.append((0, 0, 1))
            visited[0][0] = True

            while q:
                y, x, cnt = q.popleft()

                if y == n-1 and x == n-1:
                    return cnt

                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if ny >= n or nx >= n or ny < 0 or nx < 0:
                        continue
                    if grid[ny][nx] == 1:
                        continue
                    if visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    q.append((ny, nx, cnt + 1))

            return -1

        return bfs()
