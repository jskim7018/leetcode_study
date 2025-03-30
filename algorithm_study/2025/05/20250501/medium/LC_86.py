from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = None
        greater_equal_head = None

        smaller_tail = None
        greater_equal_tail = None

        while head is not None:
            node = ListNode(head.val)
            if head.val < x:
                if smaller_head is None:
                    smaller_head = node
                else:
                    smaller_tail.next = node
                smaller_tail = node
            else:
                if greater_equal_head is None:
                    greater_equal_head = node
                else:
                    greater_equal_tail.next = node
                greater_equal_tail = node
            head = head.next

        if smaller_head is not None:
            smaller_tail.next = greater_equal_head
            return smaller_head
        else:
            return greater_equal_head

