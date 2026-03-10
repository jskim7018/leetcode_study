from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min-heap 사용. heap으로 작은 값, 몇번째 linkedlist index인지 저장.
        n = len(lists)
        min_heap = []
        for i, head in enumerate(lists):
            if head is not None:
                min_heap.append((head.val, i))

        heapq.heapify(min_heap)

        ans_head = None
        ans_tail = None
        while min_heap:
            _, idx = heapq.heappop(min_heap)
            if ans_head is None:
                ans_head = lists[idx]
                ans_tail = lists[idx]
            else:
                ans_tail.next = lists[idx]
                ans_tail = lists[idx]

            lists[idx] = lists[idx].next
            if lists[idx] is not None:
                heapq.heappush(min_heap, (lists[idx].val, idx))

            ans_tail.next = None

        return ans_head
