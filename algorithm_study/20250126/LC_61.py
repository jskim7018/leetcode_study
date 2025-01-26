from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        # 1. Get size of linked list
        tmp = head
        size = 0
        while tmp is not None:
            tmp = tmp.next
            size += 1

        # 2. Get cut point
        k = k % size
        cut_point = size - k

        # 3. Connect last with first if cut_point is not 0
        tmp = head
        while tmp.next is not None:
            tmp = tmp.next

        tmp.next = head

        # 4. disconnect at cut point
        tmp = head
        if cut_point != 0:
            while cut_point > 1:
                cut_point -= 1
                tmp = tmp.next

        ans = tmp.next
        tmp.next = None

        return ans
