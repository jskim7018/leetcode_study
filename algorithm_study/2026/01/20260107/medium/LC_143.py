from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        size = 0
        tmp_head = head
        while tmp_head is not None:
            size += 1
            tmp_head = tmp_head.next
        start = math.ceil(size / 2)

        stack = list()
        prev = None
        tmp_head = head
        for i in range(size):
            head_next = tmp_head.next

            if size % 2 == 1 and i == size//2:
                tmp_head.next = None
                prev = tmp_head
            elif i < start:
                stack.append(tmp_head)
            else:
                left = stack.pop()
                left.next = tmp_head
                tmp_head.next = prev
                prev = left
            tmp_head = head_next

        return head
