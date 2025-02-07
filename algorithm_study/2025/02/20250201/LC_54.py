from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        visited = [[False for _ in range(n)] for _ in range(m)]

        ans = []
        y = 0
        x = -1

        # 0: right, 1:down, 2:left, 3:up
        def move_all(direction) -> bool:
            nonlocal y
            nonlocal x
            is_moved = False
            while True:
                ny = y + dy[direction]
                nx = x + dx[direction]
                if ny >= m or nx >= n or ny < 0 or nx < 0 or visited[ny][nx]:
                    return is_moved
                is_moved = True
                ans.append(matrix[ny][nx])
                visited[ny][nx] = True

                y = ny
                x = nx

        direction = 0
        while move_all(direction):
            direction = (direction + 1) % 4

        return ans