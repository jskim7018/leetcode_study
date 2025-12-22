from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        def canPartitionGrid(is_vertical: bool) -> bool:
            nonlocal grid

            if is_vertical:
                a = m
                b = n
            else:
                a = n
                b = m
            prefix_sum = [0] * b

            for i in range(a):
                prefix_sum_tmp = [0] * b
                for j in range(b):
                    if is_vertical:
                        prefix_sum_tmp[j] += grid[i][j]
                    else:
                        prefix_sum_tmp[j] += grid[j][i]
                    if j > 0:
                        prefix_sum_tmp[j] += prefix_sum_tmp[j - 1]
                    prefix_sum[j] += prefix_sum_tmp[j]
            for j in range(1, len(prefix_sum)):
                left_sum = prefix_sum[j - 1]
                right_sum = prefix_sum[-1] - prefix_sum[j - 1]

                if left_sum == right_sum:
                    return True

            return False

        if canPartitionGrid(True):
            return True
        else:
            return canPartitionGrid(False)
