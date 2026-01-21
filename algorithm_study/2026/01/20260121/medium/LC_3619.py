from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dy = [1,-1,0,0]
        dx = [0,0,1,-1]

        def dfs(y: int, x: int) -> int:

            ret = grid[y][x]
            grid[y][x] = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] != 0:
                    ret += dfs(ny, nx)

            return ret

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    island_val = dfs(i,j)
                    if island_val % k == 0:
                        ans += 1
        return ans
