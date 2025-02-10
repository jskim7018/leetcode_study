from typing import List

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        max_area = -1
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        rect_points = [points[i], points[j], points[k], points[l]]
                        rect_points.sort(key=lambda x: (x[0], x[1]))
                        if rect_points[0][0] == rect_points[1][0] and \
                            rect_points[2][0] == rect_points[3][0] and \
                            rect_points[0][0] != rect_points[2][0] and \
                            rect_points[0][1] == rect_points[2][1] and \
                            rect_points[1][1] == rect_points[3][1] and \
                            rect_points[0][1] != rect_points[1][1]:
                            is_good = True
                            print(rect_points)
                            for m in range(n):
                                if m == i or m == j or m == k or m == l:
                                    continue
                                if rect_points[0][0] <= points[m][0] <= rect_points[2][0] \
                                        and rect_points[0][1] <= points[m][1] <= rect_points[1][1]:
                                    print(points[m])
                                    is_good = False
                                    break
                            if is_good:
                                area = abs(rect_points[0][1] - rect_points[1][1]) * \
                                    abs(rect_points[0][0] - rect_points[2][0])
                                max_area = max(max_area, area)

        return max_area
