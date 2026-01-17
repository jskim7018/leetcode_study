from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse_reverse_odd(left: Optional[TreeNode],
                                 right: Optional[TreeNode], depth: int):
            if left is None or right is None:
                return

            if depth % 2 == 1:
                left.val, right.val = right.val, left.val

            traverse_reverse_odd(left.left, right.right, depth+1)
            traverse_reverse_odd(left.right, right.left, depth+1)

        traverse_reverse_odd(root.left, root.right, 1)

        return root
