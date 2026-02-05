from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # sorted list works. Other way than sorted list?
        ans = 0

        sorted_boxes = sorted(boxes)

        for w in warehouse:
            while sorted_boxes and sorted_boxes[-1] > w:
                sorted_boxes.pop()
            if sorted_boxes:
                sorted_boxes.pop()
                ans += 1
        return ans
