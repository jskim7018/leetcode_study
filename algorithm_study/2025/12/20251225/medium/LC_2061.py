from typing import List


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m = len(room)
        n = len(room[0])
        visited = set()
        cleaned_visited = set()

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        y = 0
        x = 0
        curr_dir = 0

        while (y, x, curr_dir) not in visited:
            if (y,x) not in cleaned_visited:
                cleaned_visited.add((y,x))
            visited.add((y, x, curr_dir))

            for i in range(4):
                ny = y + dy[(curr_dir + i) % 4]
                nx = x + dx[(curr_dir + i) % 4]
                if ny >= m or ny < 0 or nx >= n or nx < 0 or room[ny][nx] == 1:
                    continue
                else:
                    y = ny
                    x = nx
                    curr_dir = (curr_dir + i) % 4
                    break

        return len(cleaned_visited)
