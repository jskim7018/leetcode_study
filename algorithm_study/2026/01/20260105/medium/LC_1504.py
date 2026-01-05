from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            # Build histogram for row i
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Count submatrices in this histogram
            stack = []
            curr_sum = 0
            print(heights)
            for h in heights:
                count = 1
                while stack and stack[-1][0] >= h:
                    prev_h, prev_count = stack.pop()
                    curr_sum -= prev_h * prev_count
                    count += prev_count

                curr_sum += h * count
                stack.append((h, count))
                ans += curr_sum

        return ans
