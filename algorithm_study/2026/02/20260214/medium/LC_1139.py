from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # prefix_consecutive,
        # 각, row 별로 prefix consecutive cnt을 만들어 둠.
        # O(n^3) 가능. can it be one better?
        m, n = len(grid), len(grid[0])

        prefix_consecutive_row = [[0] * n for _ in range(m)]
        prefix_consecutive_col = [[0] * n for _ in range(m)]

        # col
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 0:
                    prefix_consecutive_col[i][j] = 0
                else:
                    prefix_consecutive_col[i][j] = grid[i][j]
                    if i - 1 >= 0:
                        prefix_consecutive_col[i][j] += prefix_consecutive_col[i-1][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    prefix_consecutive_row[i][j] = 0
                else:
                    prefix_consecutive_row[i][j] = grid[i][j]
                    if j-1 >= 0:
                        prefix_consecutive_row[i][j] += prefix_consecutive_row[i][j-1]

                for k in range(min(i, j), -1, -1):
                    side_len = k+1
                    if (prefix_consecutive_row[i][j] >= side_len and
                        prefix_consecutive_row[i-k][j] >= side_len and
                        prefix_consecutive_col[i][j] >= side_len and
                        prefix_consecutive_col[i][j-k] >= side_len):
                        ans = max(ans, side_len*side_len)
                        break

        return ans
