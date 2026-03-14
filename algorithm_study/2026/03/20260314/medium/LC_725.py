from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # two-pass: 1. get size, 2. make answer
        # 나머지를 구한다. 각, 그룹의 기본 크기 구한다.
        # 나머지를 하나씩 소진하면서 그룹을 만든다. (나머지 다 소진시까지.)
        # 그다음 부터는 기본으로만 그룹을 만든다.

        def get_size(head: Optional[ListNode]) -> int:
            cnt = 0
            while head:
                cnt += 1
                head = head.next

            return cnt

        n = get_size(head)

        rem = n % k
        segment_size = n // k

        ans = []

        while k:
            curr_segment_size = segment_size
            if rem > 0:
                curr_segment_size += 1
                rem -= 1

            curr_segment_head = head
            ans.append(curr_segment_head)
            for i in range(curr_segment_size):
                tmp_next = head.next
                if i == curr_segment_size-1:
                    head.next = None
                head = tmp_next

            k -= 1

        return ans
