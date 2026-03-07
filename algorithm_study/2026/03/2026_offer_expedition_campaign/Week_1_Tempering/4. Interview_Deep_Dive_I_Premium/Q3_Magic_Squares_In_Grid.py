from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def is_magic_sqr(y: int, x: int) -> bool:
            maxim = 0
            minim = float('inf')
            st = set()

            _sum_diag = 0
            _sum_opp_diag = 0
            for i in range(3):
                _sum_diag += grid[y + i][x + i]
                _sum_opp_diag += grid[y + i][x + 2 - i]

            if _sum_diag != _sum_opp_diag:
                return False

            for i in range(3):
                _sum_row = 0
                _sum_col = 0
                for j in range(3):
                    _sum_row += grid[y + i][x + j]
                    _sum_col += grid[y + j][x + i]
                    maxim = max(maxim, grid[y + i][x + j])
                    minim = min(minim, grid[y + i][x + j])
                    st.add(grid[y + i][x + j])
                if _sum_row != _sum_diag or _sum_col != _sum_diag:
                    return False

            if maxim == 9 and minim == 1 and len(st) == 9:
                return True
            else:
                return False

        m = len(grid)
        n = len(grid[0])

        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic_sqr(i, j):
                    ans += 1
        return ans
