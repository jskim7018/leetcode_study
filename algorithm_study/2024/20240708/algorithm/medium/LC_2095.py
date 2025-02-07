from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0

        tmp = head

        while head is not None:
            n+=1
            head = head.next
        # Edge case when n == 1
        if n == 1:
            return None
        middle_idx = n//2

        idx = 0
        head = tmp
        prev = tmp
        while idx != middle_idx:
            prev = head
            head = head.next
            idx += 1
        prev.next = head.next

        return tmp
