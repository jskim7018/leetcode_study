from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = head
        i = 0
        prev = None
        while tmp is not None:
            first = tmp
            second = None
            if tmp is not None and tmp.next is None:
                break
            else:
                if tmp is not None:
                    second = tmp.next
                    first.next = second.next
                    second.next = first
                    if i==0:
                        head = second

            if tmp is not None:
                tmp = first.next
            if prev is not None:
                prev.next = second

            prev = first
            i+=1

        return head
