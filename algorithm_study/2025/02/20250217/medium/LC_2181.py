from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode()
        tmp = ans
        head = head.next
        sum = 0
        while head is not None:
            if head.val != 0:
                sum += head.val
            else:
                tmp.next = ListNode(sum)
                tmp = tmp.next
                sum = 0
            head = head.next

        return ans.next