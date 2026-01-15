from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        visited = dict()

        day_cell_states = []
        start = 0
        for i in range(0, 260):
            cell_tuple = tuple(cells)
            if cell_tuple in visited:
                start = visited[cell_tuple]
                break
            visited[cell_tuple] = i
            day_cell_states.append(cell_tuple)

            new_cells = [0] * 8
            for j in range(1, 7):
                if cells[j-1] == cells[j+1]:
                    new_cells[j] = 1
            cells = new_cells
        n -= start
        n %= len(day_cell_states) - start

        return list(day_cell_states[n + start])
