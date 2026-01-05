from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for q in queries:
            top_left = (q[0], q[1])
            bot_right = (q[2], q[3])
            matrix[top_left[0]][top_left[1]] += 1
            matrix[top_left[0]][bot_right[1] + 1] -= 1
            matrix[bot_right[0] + 1][top_left[1]] -= 1
            matrix[bot_right[0] + 1][bot_right[1] + 1] += 1

        for i in range(n):
            for j in range(1, n):
                matrix[j][i] += matrix[j-1][i]
        for i in range(n):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]

        return matrix[:n][:n]
