from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0] * len(colSum) for _ in range(len(rowSum))]

        while True:
            row_max_val = max(rowSum)
            row_max_idx = rowSum.index(row_max_val)

            col_max_val = max(colSum)
            col_max_idx = colSum.index(col_max_val)

            if row_max_val == 0 and col_max_val == 0:
                break

            minim = min(row_max_val, col_max_val)
            ans[row_max_idx][col_max_idx] += minim
            rowSum[row_max_idx] -= minim
            colSum[col_max_idx] -= minim

        return ans
