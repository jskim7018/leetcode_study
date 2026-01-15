from typing import List
import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        def bfs() -> int:
            dy = [0,0,1,-1]
            dx = [1,-1,0,0]
            heap = []

            visited = [[float('inf') for _ in range(n)] for _ in range(m)]
            for i in range(4):
                heap.append((0, tuple(start), i))
                visited[start[0]][start[1]] = True

            heapq.heapify(heap)
            while heap:
                dist, curr, d = heapq.heappop(heap)
                y, x = curr

                if (y, x) == tuple(destination):
                    return dist

                ny = y + dy[d]
                nx = x + dx[d]

                traveled = 0
                while not (ny >= m or nx >= n or nx < 0 or ny < 0 or maze[ny][nx] == 1):
                    y = ny
                    x = nx
                    ny = y + dy[d]
                    nx = x + dx[d]
                    traveled += 1

                for nd in range(4):
                    if dist + traveled < visited[y][x]:
                        visited[y][x] = dist + traveled
                        heapq.heappush(heap, (dist + traveled, (y, x), nd))

            return -1

        return bfs()
