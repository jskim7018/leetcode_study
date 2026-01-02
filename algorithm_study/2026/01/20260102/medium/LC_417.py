from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def bfs() -> List[List[int]]:
            q = deque()
            visited = [[[False] * n for _ in range(m)] for _ in range(2)]
            for i in range(m):
                q.append((i,0,0))
                q.append((i,n-1,1))
                visited[0][i][0] = True
                visited[1][i][n-1] = True
            for i in range(n):
                q.append((0,i,0))
                q.append((m-1,i,1))
                visited[0][0][i] = True
                visited[1][m-1][i] = True
            print(visited[0])
            print(visited[1])
            dy = [1,-1,0,0]
            dx = [0,0,1,-1]
            while q:
                y, x, o = q.popleft()

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        continue
                    if visited[o][ny][nx]:
                        continue
                    if heights[y][x] > heights[ny][nx]:
                        continue
                    visited[o][ny][nx] = True
                    q.append((ny, nx, o))

            ans = []
            for i in range(m):
                for j in range(n):
                    if visited[0][i][j] and visited[1][i][j]:
                        ans.append([i, j])
            return ans

        return bfs()
