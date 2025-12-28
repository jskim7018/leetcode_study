from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ones_coords = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones_coords.append((i, j))

        def set_cross_value(i: int, j: int, value: int,
                            tmp_grid: List[List[int]]) -> List[List[int]]:
            row_prev = []
            col_prev = []
            for a in range(m):
                col_prev.append(tmp_grid[a][j])
                tmp_grid[a][j] = value
            for a in range(n):
                row_prev.append(tmp_grid[i][a])
                tmp_grid[i][a] = value
            return [row_prev, col_prev]

        debug = set()

        def back_tracking(curr: int) -> int:
            if curr >= len(ones_coords):
                ones_cnt = sum([sum(grid[i]) for i in range(m)])
                if ones_cnt == 0:
                    return 0
                else:
                    return float('inf')

            ret = back_tracking(curr + 1)
            y = ones_coords[curr][0]
            x = ones_coords[curr][1]
            if grid[y][x] == 1:
                row_prev, col_prev = set_cross_value(y, x, 0, grid)
                debug.add((y, x))
                ret = min(ret, back_tracking(curr + 1) + 1)
                for a in range(n):
                    grid[y][a] = row_prev[a]
                for a in range(m):
                    grid[a][x] = col_prev[a]
                debug.remove((y, x))

            return ret

        return back_tracking(0)
