from typing import List
from collections import deque, namedtuple

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m = len(rooms)
        n = len(rooms[0])

        dy = [1,-1,0,0]
        dx = [0,0,1,-1]

        def bfs(gate_list):
            visited = [[False for _ in range(n)] for _ in range(m)]

            Coord = namedtuple('Coord', ['y', 'x', 'dist'])
            q = deque()
            for gate in gate_list:
                q.append(Coord(gate[0], gate[1], 0))

            while len(q) != 0:
                c = q.popleft()

                if c.y >= m or c.x >= n or c.y < 0 or c.x < 0:
                    continue
                if rooms[c.y][c.x] == -1:
                    continue
                if visited[c.y][c.x]:
                    continue
                if rooms[c.y][c.x] == 0 and c.dist != 0:
                    continue

                visited[c.y][c.x] = True
                if c.dist != 0 and rooms[c.y][c.x] != 0:
                    if rooms[c.y][c.x] > c.dist:
                        rooms[c.y][c.x] = c.dist
                    else:
                        continue

                for i in range(4):
                    ny = c.y + dy[i]
                    nx = c.x + dx[i]

                    q.append(Coord(ny, nx, c.dist + 1))

        gate_list = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gate_list.append((i,j))
        bfs(gate_list)
