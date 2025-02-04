from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        def bfs() -> int:
            q = deque()
            q.append((entrance[0], entrance[1], 0))

            visited = [[False for _ in range(n)] for _ in range(m)]

            dy = [0,0,-1,1]
            dx = [-1,1,0,0]
            while q:
                coord = q.popleft()
                y = coord[0]
                x = coord[1]
                move = coord[2]

                if maze[y][x] == "+":
                    continue
                if visited[y][x]:
                    continue

                visited[y][x] = True

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if ny >= m or nx >= n or ny < 0 or nx < 0:
                        if [y, x] != entrance:
                            return move
                        else:
                            continue
                    q.append((ny,nx,move+1))
            return -1

        return bfs()
