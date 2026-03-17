from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Sentinel to flush stack at the end

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            heights.pop()  # Restore
            return max_area

        n_cols = len(matrix[0])
        heights = [0] * n_cols
        max_area = 0

        for row in matrix:
            for j in range(n_cols):
                # Update histogram heights
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            # Compute largest rectangle in this row's histogram
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
