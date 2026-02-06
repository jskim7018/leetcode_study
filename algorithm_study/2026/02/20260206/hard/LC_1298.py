from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        # 연 박스는 더이상 필요 없다.
        # 연 박스에서 나온 박스들을 어딘가 저장해둔다. (set)
        # 박스에서 key가 나오면 바로 status를 변경해준다.
        # 새로운 박스 혹은 key가 나오면 모든 박스들을 loop를 돌면서 다시 확인한다.
        # 언제 멈추나? (새로운 박스 혹은 key가 안나오면 멈춘다.)

        not_opened_boxes = set(initialBoxes)
        ans = 0
        # TODO: open 가능한 박스만 loop 하도록 수정 하면 더 효율적.
        while not_opened_boxes:
            opened_boxes = set()
            new_boxes = set()
            for box in not_opened_boxes:
                if status[box] == 1:
                    for key in keys[box]:
                        status[key] = 1
                    new_boxes.update(containedBoxes[box])
                    ans += candies[box]
                    opened_boxes.add(box)
            not_opened_boxes.update(new_boxes)
            if not opened_boxes:
                break
            not_opened_boxes -= opened_boxes

        return ans

# ChatGpt code:
from collections import deque
from typing import List

# class Solution:
#     def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
#         q = deque()
#         have_box = set(initialBoxes)
#         opened = set()
#         total = 0
#
#         for b in initialBoxes:
#             if status[b] == 1:
#                 q.append(b)
#                 opened.add(b)
#
#         while q:
#             box = q.popleft()
#             total += candies[box]
#
#             for k in keys[box]:
#                 status[k] = 1
#                 if k in have_box and k not in opened:
#                     q.append(k)
#                     opened.add(k)
#
#             for b in containedBoxes[box]:
#                 have_box.add(b)
#                 if status[b] == 1 and b not in opened:
#                     q.append(b)
#                     opened.add(b)
#
#         return total
