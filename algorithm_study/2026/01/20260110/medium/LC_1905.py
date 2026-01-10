from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        def check_dfs(y: int, x: int) -> bool:
            ret = True
            for a in range(4):
                ny = y + dy[a]
                nx = x + dx[a]

                if 0 <= ny < m and 0 <= nx < n and grid2[ny][nx] == 1 and \
                        not visited[ny][nx]:
                    visited[ny][nx] = True
                    if grid1[ny][nx] != 1:
                        ret &= False
                    check = check_dfs(ny, nx)
                    ret &= check
            return ret

        visited = [[False for _ in range(n)] for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if (grid2[i][j] == 1 and grid1[i][j] and not visited[i][j]):
                    visited[i][j] = True
                    if check_dfs(i, j):
                        cnt += 1

        return cnt
