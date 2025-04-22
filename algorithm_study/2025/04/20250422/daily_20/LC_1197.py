from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dy = [2,2,-2,-2,1,1,-1,-1]
        dx = [1,-1,1,-1,2,-2,2,-2]

        def bfs() -> int:
            q = deque()
            visited = set()
            q.append((0,0,0))
            visited.add((0, 0))

            while q:
                popped = q.popleft()
                cy = popped[0]
                cx = popped[1]
                moves = popped[2]


                if cy == y and cx == x:
                    return moves

                for i in range(8):
                    ny = cy + dy[i]
                    nx = cx + dx[i]
                    if (ny, nx) not in visited:
                        visited.add((ny, nx))
                        q.append((ny, nx, moves+1))

        return bfs()
