from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # TODO: multi source bfs. 매우 흥미롭고 재밌는 문제.
        def bfs() -> int:
            dy = [1,-1,0,0]
            dx = [0,0,1,-1]

            q = deque()
            ret = 0
            visited = [[False] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        q.append((i, j, 0))
                        visited[i][j] = True

            if not q or len(q) == n*n:
                return -1

            while q:
                y, x, dist = q.popleft()
                ret = dist

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= n or nx >= n or ny < 0 or nx < 0:
                        continue
                    if visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    q.append((ny,nx,dist + 1))

            return ret

        return bfs()
