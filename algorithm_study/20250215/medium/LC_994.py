from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0

        rotten_oranges = []
        fresh_oranges = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges.append((i,j))
        visited = [[False for _ in range(n)] for _ in range(m)]
        def bfs(rotten_oranges, visited):
            nonlocal ans

            q = deque()
            for rotten in rotten_oranges:
                q.append((rotten[0], rotten[1], 0))

            dy = [0,0,-1,1]
            dx = [-1,1,0,0]
            while q:
                coord = q.popleft()
                y = coord[0]
                x = coord[1]
                minutes = coord[2]

                if y >= m or x >= n or y < 0 or x < 0:
                    continue
                if grid[y][x] == 0:
                    continue
                if visited[y][x]:
                    continue
                visited[y][x] = True
                ans = max(ans, minutes)

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    q.append((ny,nx,minutes+1))

        bfs(rotten_oranges, visited)

        for fresh in fresh_oranges:
            if not visited[fresh[0]][fresh[1]]:
                return -1

        return ans
