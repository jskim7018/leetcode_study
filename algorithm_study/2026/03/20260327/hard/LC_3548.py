from typing import List
from collections import defaultdict


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        row_prefix_sum = [0] * m
        col_prefix_sum = [0] * n

        num_coords = defaultdict(list)

        for i in range(m):
            row_prefix_sum[i] += sum(grid[i])
            if i - 1 >= 0:
                row_prefix_sum[i] += row_prefix_sum[i - 1]

        for j in range(n):
            col_sum = 0
            for i in range(m):
                num_coords[grid[i][j]].append((i, j))
                col_sum += grid[i][j]
            col_prefix_sum[j] += col_sum
            if j - 1 >= 0:
                col_prefix_sum[j] += col_prefix_sum[j - 1]

        def check_if_not_disconnect(y, x, x_lower_bound, x_upper_bound,
                                    y_lower_bound, y_upper_bound) -> bool:
            if x - 1 >= x_lower_bound and x + 1 <= x_upper_bound:
                if y + 1 > y_upper_bound and y - 1 < y_lower_bound:
                    return False
            if y - 1 >= y_lower_bound and y + 1 <= y_upper_bound:
                if x - 1 < x_lower_bound and x + 1 > x_upper_bound:
                    return False

            return True

        for i in range(m - 1):
            upper_sum = row_prefix_sum[i]
            lower_sum = row_prefix_sum[m - 1] - row_prefix_sum[i]

            if upper_sum == lower_sum:
                return True

            is_upper_bigger = False
            if upper_sum > lower_sum:
                diff = upper_sum - lower_sum
                is_upper_bigger = True
            else:
                diff = lower_sum - upper_sum

            for y, x in num_coords[diff]:
                if is_upper_bigger and y > i:
                    continue
                if not is_upper_bigger and y <= i:
                    continue

                if i+1 > 1 and m - (i + 1) > 1 and n > 1:
                    return True

                y_lower_bound = 0
                y_upper_bound = i

                if not is_upper_bigger:
                    y_lower_bound = i + 1
                    y_upper_bound = m - 1
                if check_if_not_disconnect(y, x, 0, n - 1, y_lower_bound, y_upper_bound):
                    return True

        for i in range(n - 1):
            left_sum = col_prefix_sum[i]
            right_sum = col_prefix_sum[n - 1] - col_prefix_sum[i]

            if left_sum == right_sum:
                return True

            is_left_bigger = False
            if left_sum > right_sum:
                diff = left_sum - right_sum
                is_left_bigger = True
            else:
                diff = right_sum - left_sum

            for y, x in num_coords[diff]:
                if is_left_bigger and x > i:
                    continue
                if not is_left_bigger and x <= i:
                    continue

                if i+1 > 1 and n - (i + 1) > 1 and m > 1:
                    return True

                x_lower_bound = 0
                x_upper_bound = i

                if not is_left_bigger:
                    x_lower_bound = i + 1
                    x_upper_bound = n - 1

                if check_if_not_disconnect(y, x, x_lower_bound, x_upper_bound, 0, m - 1):
                    return True

        return False