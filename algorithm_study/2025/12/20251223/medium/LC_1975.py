from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        neg_cnt = 0
        minim = float('inf')

        max_sum = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    neg_cnt += 1

                minim = min(minim, abs(matrix[i][j]))
                max_sum += abs(matrix[i][j])

        if neg_cnt % 2 == 1:
            max_sum -= minim * 2

        return max_sum
