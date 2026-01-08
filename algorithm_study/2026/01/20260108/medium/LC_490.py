from typing import List
from collections import deque


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])

        def bfs() -> bool:
            dy = [0,0,1,-1]
            dx = [1,-1,0,0]
            q = deque()

            visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(m)]
            for i in range(4):
                q.append((start, i))
                visited[start[0]][start[1]][i] = True

            while q:
                curr, d = q.popleft()
                y, x = curr

                ny = y + dy[d]
                nx = x + dx[d]

                while not (ny >= m or nx >= n or nx < 0 or ny < 0 or maze[ny][nx] == 1):
                    y = ny
                    x = nx
                    ny = y + dy[d]
                    nx = x + dx[d]

                if (y, x) == tuple(destination):
                    return True

                for nd in range(4):
                    if not visited[y][x][nd]:
                        visited[y][x][nd] = True
                        q.append(((y, x), nd))

            return False

        return bfs()
