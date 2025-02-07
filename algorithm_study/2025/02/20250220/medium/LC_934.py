from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island1_coords = []

        visited = [[False for _ in range(n)] for _ in range(n)]
        dy = [1,-1, 0,0]
        dx = [0,0,1,-1]
        def dfs(y, x):
            if y >= n or x >= n or y < 0 or x < 0:
                return
            if grid[y][x] == 0:
                return
            if visited[y][x]:
                return
            visited[y][x] = True

            if grid[y][x] == 1:
                island1_coords.append((y,x))

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                dfs(ny, nx)


        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                if island1_coords:
                    break
            if island1_coords:
                break


        def bfs(coords) -> int:
            q = deque()
            for c in coords:
                q.append((c[0], c[1], 0))

            while q:
                c = q.popleft()
                y = c[0]
                x = c[1]
                dist = c[2]

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= n or nx >= n or ny < 0 or nx < 0:
                        continue
                    if visited[ny][nx]:
                        continue
                    if grid[ny][nx] == 1:
                        return dist
                    visited[ny][nx] = True
                    q.append((ny,nx,dist+1))

        return bfs(island1_coords)
