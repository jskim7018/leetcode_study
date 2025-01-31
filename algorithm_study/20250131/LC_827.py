from typing import List
from pprint import pprint

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dy = [1,-1,0,0]
        dx = [0,0,1,-1]

        id_to_area = dict()
        def dfs(y, x, id, area) -> int:
            if y >= m or x >=n or y < 0 or x < 0:
                return 0

            if grid[y][x] != 1 or grid[y][x] == 0:
                return 0

            grid[y][x] = id

            ret = 1
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                ret += dfs(ny, nx, id, area)
            return ret

        id = 2
        for i in range(m):
            for j in range(n):
                ret = dfs(i, j, id, 0)
                if ret != 0:
                    id_to_area[id] = ret
                id += 1

        ans = 0
        is_zero_exist = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    is_zero_exist = True
                    sum = 1
                    already = set()
                    for a in range(4):
                        ny = i + dy[a]
                        nx = j + dx[a]
                        if ny >= m or nx >= n or ny < 0 or nx < 0:
                            continue
                        if grid[ny][nx] not in already:
                            sum += id_to_area.get(grid[ny][nx], 0)
                            already.add(grid[ny][nx])
                    ans = max(ans, sum)
        if is_zero_exist:
            return ans
        else:
            return m*n
