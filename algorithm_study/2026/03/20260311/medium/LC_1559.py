from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # 각, DFS 하면서 위치 처음 방문한 step 기록.
        # 다시 해당 위치 방문 가능한 node 왔을때 거리 확인. 거리가 3차이 이상 나면 True
        # 이미 갔던데를 가지만 않고 아무 싸이클이라도 있으면 무조건 정답.
        m, n = len(grid), len(grid[0])

        dy = [0,0,-1,1]
        dx = [-1,1,0,0]

        visited_step = [[-1] * n for _ in range(m)]

        def dfs(y: int, x: int, step: int) -> bool:
            ret = False
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny >= m or nx >= n or ny < 0 or nx < 0:
                    continue
                if grid[ny][nx] == grid[y][x]:
                    if visited_step[ny][nx] == -1:
                        visited_step[ny][nx] = step+1
                        ret |= dfs(ny, nx, step+1)
                    else:
                        if step - visited_step[ny][nx] >= 3:
                            return True

            return ret

        for i in range(m):
            for j in range(n):
                visited_step[i][j] = 0
                if dfs(i, j, 0):
                    return True

        return False
