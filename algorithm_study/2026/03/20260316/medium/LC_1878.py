from typing import List
import pytest


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # create prefix_sum for the two diagonals
        # iterate over all spots and check all possible rhombus size
        # O(n*n*n) => O(n^2)

        m, n = len(grid), len(grid[0])

        right_diag_sums = [[0] * n for _ in range(m)]
        left_diag_sums = [[0] * n for _ in range(m)]

        def preprocess():
            for i in range(1, m):
                y = i
                x = 0
                while y < m and x < n:
                    right_diag_sums[y][x] = grid[y][x]
                    if y - 1 >= 0 and x-1 >=0:
                        right_diag_sums[y][x] += right_diag_sums[y-1][x-1]
                    y += 1
                    x += 1
                y = i
                x = n-1
                while y < m and x >= 0:
                    left_diag_sums[y][x] = grid[y][x]
                    if y - 1 >= 0 and x + 1 < n:
                        left_diag_sums[y][x] += left_diag_sums[y - 1][x + 1]
                    y += 1
                    x -= 1

            for j in range(n):
                x = j
                y = 0

                while x < n and y < m:
                    while y < m and x < n:
                        right_diag_sums[y][x] = grid[y][x]
                        if y - 1 >= 0 and x - 1 >= 0:
                            right_diag_sums[y][x] += right_diag_sums[y - 1][x - 1]
                        y += 1
                        x += 1

                x = j
                y = 0
                while y < m and x >= 0:
                    left_diag_sums[y][x] = grid[y][x]
                    if y - 1 >= 0 and x + 1 < n:
                        left_diag_sums[y][x] += left_diag_sums[y - 1][x + 1]
                    y += 1
                    x -= 1

        preprocess()

        ans = set()
        for i in range(m):
            for j in range(n):
                k = 0
                while i + 2 * k < m and j - k >= 0 and j + k < n:
                    if k == 0:
                        total = grid[i][j]
                    else:
                        right_diags_total = right_diag_sums[i+k][j+k] + right_diag_sums[i+2*k][j]
                        left_diags_total = 0
                        if i+k-1 >= 0 and j-k+1 < n:
                            left_diags_total += left_diag_sums[i+k-1][j-k+1]
                            left_diags_total -= left_diag_sums[i][j]
                        if i+2*k-1>=0 and j+1 < n:
                            left_diags_total += left_diag_sums[i+2*k-1][j+1]
                            left_diags_total -= left_diag_sums[i + k][j + k]
                        if i-1 >= 0 and j-1 >= 0:
                            right_diags_total -= right_diag_sums[i-1][j-1]
                        if i+k-1 >= 0 and j-k-1 >= 0:
                            right_diags_total -= right_diag_sums[i+k-1][j-k-1]
                        total = right_diags_total + left_diags_total
                    ans.add(total)
                    k += 1

        ans = list(ans)

        ans.sort(reverse=True)
        if len(ans) < 3:
            return ans
        else:
            return ans[:3]


@pytest.mark.parametrize("input_grid, expected", [
    ([[1,2,3],[4,5,6],[7,8,9]], [20,9,8]),
    ([[7,7,7]], [7])
])
def test_getBiggestThree(input_grid, expected):
    sol = Solution()
    assert sol.getBiggestThree(input_grid) == expected
