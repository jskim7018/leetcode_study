from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        st = set()
        visited = [[False]*n for _ in range(m)]

        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        s = ""
        def dfs(i, j, init_i, init_j):
            nonlocal s
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0:
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            s += f'({i-init_i},{j-init_j})'

            for x in range(4):
                ny = dy[x] + i
                nx = dx[x] + j
                dfs(ny, nx, init_i, init_j)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    s = ""
                    dfs(i,j, i, j)
                    st.add(s)
        return len(st)
