from typing import Optional
import heapq


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:

        ans = 0
        def traverse(node: 'Node') -> int:
            nonlocal ans

            if node is None:
                return 0

            maxim = 0
            second_max = 0
            heap = []
            for c in node.children:
                heap.append(-(traverse(c)+1))

            heapq.heapify(heap)
            if heap:
                maxim = -heapq.heappop(heap)
            if heap:
                second_max = -heapq.heappop(heap)

            ans = max(ans, maxim + second_max)

            return maxim

        traverse(root)
        return ans
