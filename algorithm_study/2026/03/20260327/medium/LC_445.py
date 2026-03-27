from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # stack 활용
        l1_stck = []
        l2_stck = []

        while l1 or l2:
            if l1:
                l1_stck.append(l1.val)
                l1 = l1.next
            if l2:
                l2_stck.append(l2.val)
                l2 = l2.next

        prev_head = None
        carry = 0
        while l1_stck or l2_stck or carry:
            l1_val = 0
            l2_val = 0
            if l1_stck:
                l1_val = l1_stck.pop()
            if l2_stck:
                l2_val = l2_stck.pop()

            _sum = l1_val + l2_val + carry
            carry = _sum // 10
            _sum %= 10

            node = ListNode(_sum, prev_head)
            prev_head = node

        return prev_head
