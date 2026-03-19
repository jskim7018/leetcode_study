class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # 2-pass면 쉽게 가능.
        # 1-pass possible? No

        tmp_head = head
        one_set = set()
        dup_set = set()

        while tmp_head is not None:
            if tmp_head.val in one_set:
                dup_set.add(tmp_head.val)
            else:
                one_set.add(tmp_head.val)
            tmp_head = tmp_head.next

        tmp_head = head
        prev = None
        ret_head = head
        while tmp_head is not None:
            val = tmp_head.val
            if val in dup_set:
                if prev is not None:
                    prev.next = tmp_head.next
                else:
                    ret_head = tmp_head.next
            else:
                prev = tmp_head
            tmp_head = tmp_head.next

        return ret_head
