class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def dist(coord, coord2) -> float:
            ret = ((coord[0] - coord2[0]) ** 2 + (coord[1] - coord2[1]) ** 2) ** 0.5
            return ret

        coord_circle = xCenter, yCenter
        top_left = x1, y2
        top_right = x2, y2
        bottom_left = x1, y1
        bottom_right = x2, y1
        if ((x1 - radius <= xCenter <= x2 + radius and y1 <= yCenter <= y2) or
                (y1 - radius <= yCenter <= y2 + radius and x1 <= xCenter <= x2) or
            dist(coord_circle, top_left) <= radius or dist(coord_circle, top_right) <= radius or
            dist(coord_circle, bottom_left) <= radius or dist(coord_circle, bottom_right) <= radius):
            return True
        else:
            return False

# Chatgpt solution TODO: 제대로 파악하기.
# class Solution:
#     def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
#         # Clamp circle center to rectangle
#         closest_x = min(max(xCenter, x1), x2)
#         closest_y = min(max(yCenter, y1), y2)
#
#         # Compute squared distance
#         dx = xCenter - closest_x
#         dy = yCenter - closest_y
#
#         return dx * dx + dy * dy <= radius * radius
