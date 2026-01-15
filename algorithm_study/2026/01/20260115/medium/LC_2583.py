from typing import Optional
from collections import defaultdict
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        depth_to_sum = defaultdict(int)

        def traverse(node: Optional[TreeNode], depth: int):
            if not node:
                return

            depth_to_sum[depth] += -node.val

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)

        lst = list(depth_to_sum.values())
        heapq.heapify(lst)

        ans = -1
        while k and lst:
            k -= 1
            popped = -heapq.heappop(lst)
            if k == 0:
                ans = popped

        return ans
