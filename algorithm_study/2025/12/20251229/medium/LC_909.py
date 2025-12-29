from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        dir_x = 0
        dir_y = 0
        curr_y = m-1
        curr_x = 0

        mp_num_to_coord = dict()

        for i in range(1, m*n+1):
            mp_num_to_coord[i] = (curr_y, curr_x)
            if dir_x != 0 and ((curr_x == n-1 and dir_y == 0) or (curr_x == 0 and dir_y == 0)):
                dir_x = 0
                dir_y = -1
            elif dir_x == 0:
                if curr_x == 0:
                    dir_x = 1
                    dir_y = 0
                elif curr_x == n-1:
                    dir_x = -1
                    dir_y = 0
            curr_x += dir_x
            curr_y += dir_y

        def bfs(start: int) -> int:
            queue = deque()

            queue.append((start, 0))
            visited = [[False] * (m*n+1) for _ in range(2)]
            visited[0][start] = True
            visited[1][start] = True

            while queue:
                curr_pos, curr_time = queue.popleft()

                if curr_pos == m*n:
                    return curr_time

                for i in range(1, 7):
                    next_pos = curr_pos + i
                    if next_pos > m*n:
                        continue
                    if visited[0][next_pos]:
                        continue
                    next_y, next_x = mp_num_to_coord[next_pos]
                    visited[0][next_pos] = True
                    next_board_val = board[next_y][next_x]
                    if next_board_val != -1 and not visited[1][next_board_val]:
                        visited[1][next_board_val] = True
                        queue.append((next_board_val, curr_time + 1))
                    elif next_board_val == -1:
                        queue.append((next_pos, curr_time + 1))
            return -1

        return bfs(1)
