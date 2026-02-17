from typing import List
from collections import deque


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # simple bfs
        start_y = -1
        start_x = -1

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    start_y = i
                    start_x = j
                    break
            if start_y != -1:
                break

        def bfs() -> int:
            dy = [1,-1,0,0]
            dx = [0,0,1,-1]

            visited = [[False] * n for _ in range(m)]
            q = deque()
            q.append((start_y, start_x, 0))
            visited[start_y][start_x] = True

            while q:
                y, x, dist = q.popleft()

                if grid[y][x] == '#':
                    return dist

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if ny >= m or nx >=n or ny < 0 or nx < 0:
                        continue
                    if grid[ny][nx] == 'X':
                        continue
                    if visited[ny][nx]:
                        continue

                    visited[ny][nx] = True

                    q.append((ny, nx, dist + 1))

            return -1

        return bfs()
