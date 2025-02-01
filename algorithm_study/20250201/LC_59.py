from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = n

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        visited = [[False for _ in range(n)] for _ in range(m)]

        ans = [[0 for _ in range(n)] for _ in range(n)]
        y = 0
        x = -1
        cnt = 1

        # 0: right, 1:down, 2:left, 3:up
        def move_all(direction) -> bool:
            nonlocal y
            nonlocal x
            nonlocal cnt
            is_moved = False
            while True:
                ny = y + dy[direction]
                nx = x + dx[direction]
                if ny >= m or nx >= n or ny < 0 or nx < 0 or visited[ny][nx]:
                    return is_moved
                is_moved = True
                ans[ny][nx] = cnt
                cnt+=1
                visited[ny][nx] = True

                y = ny
                x = nx

        direction = 0
        while move_all(direction):
            direction = (direction + 1) % 4

        return ans