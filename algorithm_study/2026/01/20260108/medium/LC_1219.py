from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dy = [0,0,1,-1]
        dx = [1,-1,0,0]

        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(y: int, x: int) -> int:
            ret = grid[y][x]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny >= m or nx >= n or ny < 0 or nx < 0:
                    continue
                if not visited[ny][nx] and grid[ny][nx] != 0:
                    visited[ny][nx] = True
                    ret = max(ret, dfs(ny, nx) + grid[y][x])
                    visited[ny][nx] = False
            return ret

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    visited[i][j] = True
                    ans = max(ans, dfs(i,j))
                    visited[i][j] = False
        return ans
