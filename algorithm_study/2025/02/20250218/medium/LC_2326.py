from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(m)]

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        visited = [[False for _ in range(n)] for _ in range(m)]

        y = 0
        x = -1

        # 0: right, 1:down, 2:left, 3:up
        def move_all(direction) -> bool:
            nonlocal y
            nonlocal x
            nonlocal head
            is_moved = False
            while True:
                ny = y + dy[direction]
                nx = x + dx[direction]
                if ny >= m or nx >= n or ny < 0 or nx < 0 or visited[ny][nx]:
                    return is_moved
                is_moved = True
                if head is not None:
                    ans[ny][nx] = head.val
                    head = head.next
                else:
                    ans[ny][nx] = -1
                visited[ny][nx] = True

                y = ny
                x = nx

        direction = 0
        while move_all(direction):
            direction = (direction + 1) % 4

        return ans
