class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left_connect = None
        right_connect = None

        i = 0
        tmp_list1 = list1
        while tmp_list1 is not None:
            if i == a-1:
                left_connect = tmp_list1
            if i == b+1:
                right_connect = tmp_list1
            tmp_list1 = tmp_list1.next
            i += 1

        if left_connect is not None:
            left_connect.next = list2

        while list2 is not None:
            if list2.next is None:
                list2.next = right_connect
                break
            list2 = list2.next

        return list1
