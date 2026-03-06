from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs() -> int:
            dy = [0,0,1,-1]
            dx = [1,-1,0,0]

            visited = [[False] * n for _ in range(m)]

            q = deque()
            fresh_cnt = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        q.append((i,j,0))
                    elif grid[i][j] == 1:
                        fresh_cnt += 1
            ans = 0
            while q:
                y, x, time = q.popleft()
                ans = time
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        continue
                    if visited[ny][nx]:
                        continue
                    if grid[ny][nx] != 1:
                        continue

                    visited[ny][nx] = True
                    fresh_cnt -= 1
                    q.append((ny,nx,time + 1))
            if fresh_cnt != 0:
                return -1
            else:
                return ans

        return bfs()
