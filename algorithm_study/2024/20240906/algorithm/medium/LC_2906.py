from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        all_mult = 1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                all_mult *= grid[i][j]
                all_mult %= MOD

        grid_ans = []
        print(all_mult)
        for i in range(0,len(grid)):
            row = []
            for j in range(0, len(grid[i])):
                row.append(int((all_mult/grid[i][j])) % MOD)

            grid_ans.append(row)

        return grid_ans
