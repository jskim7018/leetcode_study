from typing import List
from heapq import *


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]

        visited = [[False] * n for _ in range(m)]
        def solve():
            heap = []
            heap.append((-grid[0][0], 0, 0))
            visited[0][0] = True
            while heap:
                element = heappop(heap)
                val = -element[0]
                y = element[1]
                x = element[2]

                if y == m-1 and x == n-1:
                    return val

                visited[y][x] = True

                for a in range(4):
                    ny = dy[a] + y
                    nx = dx[a] + x
                    if ny < 0 or nx < 0 or ny >= m or nx >= n:
                        continue
                    if visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    heappush(heap, (-min(val, grid[ny][nx]),ny, nx))

        return solve()
