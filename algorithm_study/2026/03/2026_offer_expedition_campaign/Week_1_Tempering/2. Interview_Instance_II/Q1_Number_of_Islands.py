from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dy = [0,0,-1,1]
        dx = [1,-1,0,0]

        visited = [[False] * n for _ in range(m)]

        def dfs(y: int, x: int):
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if ny >= m or nx >= n or ny < 0 or nx < 0:
                    continue
                if grid[ny][nx] == '1' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dfs(ny, nx)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j)
                    ans += 1
        return ans
