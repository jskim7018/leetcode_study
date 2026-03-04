from typing import List
import pytest


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        histogram_matrix = [[0] * n for _ in range(m)]

        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 1:
                    histogram_matrix[i][j] = 1
                    if i - 1 >= 0:
                        histogram_matrix[i][j] += histogram_matrix[i-1][j]
        ans = 0
        for i in range(m):
            row = histogram_matrix[i]
            row.sort()
            curr_cnt = len(row)
            for r in row:
                ans = max(ans, curr_cnt * r)
                curr_cnt -= 1

        return ans


@pytest.mark.parametrize("input_matrix, expected", [
    ([[0,0,1],[1,1,1],[1,0,1]], 4),
    ([[1,0,1,0,1]], 3),
    ([[1,1,0],[1,0,1]], 2)
])
def test_largestSubmatrix(input_matrix, expected):
    sol = Solution()

    assert sol.largestSubmatrix(input_matrix) == expected
