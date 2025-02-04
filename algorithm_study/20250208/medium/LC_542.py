from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]

        def bfs():
            nonlocal ans
            q = deque()
            visited = [[False for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 0:
                        q.append((i,j,0))

            dy = [1,-1,0,0]
            dx = [0,0,1,-1]
            while len(q) != 0:
                coord = q.popleft()
                y = coord[0]
                x = coord[1]
                val = coord[2]

                if y >= m or x >= n or y < 0 or x < 0:
                    continue
                if visited[y][x]:
                    continue

                ans[y][x] = val

                visited[y][x] = True

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    q.append((ny,nx, val+1))
        bfs()
        return ans
