from typing import Optional


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = head
            head = head.next
            prev.next = None
            while head:
                head_next = head.next
                head.next = prev
                prev = head
                head = head_next

            return prev

        head = reverse(head)
        tmp_head = head
        carry = 0
        tail = head
        while head:
            double_head_val = head.val * 2 + carry
            head.val = double_head_val % 10
            carry = double_head_val // 10
            tail = head
            head = head.next

        if carry == 1:
            tail.next = ListNode(carry)

        return reverse(tmp_head)
