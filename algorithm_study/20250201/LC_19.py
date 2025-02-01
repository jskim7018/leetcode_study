from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_list = []

        size = 0
        tmp = head
        while tmp is not None:
            nodes_list.append(tmp)
            tmp = tmp.next
            size += 1

        xth_node = size-n

        if xth_node != 0 and xth_node != size:
            if xth_node == size-1:
                nodes_list[xth_node - 1].next = None
            else:
                nodes_list[xth_node - 1].next = nodes_list[xth_node + 1]
            return head

        else:
            if head is not None:
                return head.next
            else:
                return None
