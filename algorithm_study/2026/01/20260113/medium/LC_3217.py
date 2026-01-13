from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_st = set(nums)

        curr = head
        prev = None

        while curr:
            nxt = curr.next
            if curr.val in nums_st:
                if prev:
                    prev.next = nxt
                else:
                    head = nxt
            else:
                prev = curr
            curr = nxt

        return head
