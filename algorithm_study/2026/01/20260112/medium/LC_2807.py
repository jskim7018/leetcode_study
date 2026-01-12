from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original_head = head

        while head is not None and head.next is not None:
            head_next = head.next
            a = head.val
            b = head.next.val

            _gcd = math.gcd(a, b)
            gcd_node = ListNode(_gcd, head.next)
            head.next = gcd_node
            head = head_next

        return original_head
