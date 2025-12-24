from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_dist = float('inf')
        max_dist = -1

        prev = head.val
        head = head.next
        first_cp = -1
        prev_cp = -1
        i = 0
        while head is not None:
            if head.next is None:
                break
            else:
                if prev < head.val > head.next.val \
                        or prev > head.val < head.next.val:
                    if first_cp == -1:
                        first_cp = i
                    else:
                        max_dist = max(max_dist, i - first_cp)
                    if prev_cp != -1:
                        min_dist = min(min_dist, i-prev_cp)
                    prev_cp = i
            prev = head.val
            head = head.next
            i += 1
        if min_dist == float('inf'):
            min_dist = -1
        return [min_dist, max_dist]
