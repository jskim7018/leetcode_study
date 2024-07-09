from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        while head is not None:
            nodes.append(head.val)
            head = head.next

        ans = 0
        for i in range(len(nodes)//2):
            ans = max(ans, nodes[i] + nodes[len(nodes)-1-i])
        return ans
