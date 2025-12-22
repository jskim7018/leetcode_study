from typing import List


class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        grid_len = 2 ** n
        grid = [[0] * grid_len for _ in range(grid_len)]

        def solve(n, y: int, x: int, start: int, end: int):
            if start == end:
                grid[y][x] = start
                return
            next_size = n-1
            next_num_size = (end-start+1)//4

            solve(next_size, y, x + int(2 ** next_size), start, start + next_num_size-1)
            start = start + next_num_size
            solve(next_size, y + int(2 ** next_size), x + int(2 ** next_size), start, start + next_num_size-1)
            start = start + next_num_size
            solve(next_size, y + int(2 ** next_size), x, start, start + next_num_size-1)
            start = start + next_num_size
            solve(next_size, y, x, start, start + next_num_size-1)

        solve(n, 0, 0, 0, 2 ** (2 * n) - 1)

        return grid
