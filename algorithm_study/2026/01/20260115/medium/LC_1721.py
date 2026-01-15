from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth = None
        kth_back = head

        idx = 1
        tmp_head = head
        while idx < k:
            tmp_head = tmp_head.next
            idx += 1
        kth = tmp_head

        while tmp_head.next:
            kth_back = kth_back.next
            tmp_head = tmp_head.next

        kth.val, kth_back.val = kth_back.val, kth.val

        return head
