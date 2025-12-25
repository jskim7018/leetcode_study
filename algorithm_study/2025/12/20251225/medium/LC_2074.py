from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret_head = head

        curr_group_len = 1

        def reverse_linked_list(head: Optional[ListNode], size: int):
            _prev = head
            _curr = head.next
            _next = head.next.next
            for i in range(size - 1):
                _curr.next = _prev
                _prev = _curr
                _curr = _next
                if _next is not None:
                    _next = _next.next

        prev_head = Optional[ListNode]
        while head is not None:
            group_start_head = head
            group_end_head = head

            actual_group_cnt = 0
            for i in range(curr_group_len):
                if head is not None:
                    group_end_head = head
                head = head.next
                actual_group_cnt += 1
                if head is None:
                    break

            if actual_group_cnt % 2 == 0:
                reverse_linked_list(group_start_head, actual_group_cnt)
                if prev_head is not None:
                    prev_head.next = group_end_head
                group_start_head.next = head
                prev_head = group_start_head
            else:
                prev_head = group_end_head
            curr_group_len += 1

        return ret_head
