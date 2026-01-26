class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stck = []
        original_head = head
        while head is not None:
            stck.append(head)
            head = head.next
        carry = 1
        # TODO: reverse -> add -> reverse 방식도 있다. space를 적게씀.
        while carry:
            if not stck:
                original_head = ListNode(1, original_head)
                carry = 0
            else:
                node = stck.pop()
                carry = (node.val + 1) // 10
                node.val = (node.val + 1) % 10

        return original_head
