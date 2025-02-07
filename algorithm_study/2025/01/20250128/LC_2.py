from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        l3 = ListNode()
        l3_head = l3
        while l1 != None or l2 != None or carry == 1:
            new_val = 0
            if l1 is not None:
                new_val += l1.val
                l1 = l1.next
            if l2 is not None:
                new_val += l2.val
                l2 = l2.next

            new_val += carry

            carry = new_val // 10
            new_val %= 10
            l3.next = ListNode(new_val)
            l3 = l3.next

        return l3_head.next
