from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = list()

        while head is not None:
            if not stack:
                stack.append(head)
            else:
                while stack and stack[-1].val < head.val:
                    stack.pop()
                if stack and stack[-1].val >= head.val:
                    stack[-1].next = head
                stack.append(head)

            head = head.next

        return stack[0]
