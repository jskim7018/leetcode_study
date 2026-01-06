from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level_to_vals = []

        def traverse(node: Optional[TreeNode], level: int) -> bool:
            if node is None:
                return True

            if level % 2 == node.val % 2:
                return False
            if len(level_to_vals) <= level:
                level_to_vals.append(node.val)
            else:
                if level % 2 == 0 and level_to_vals[level] >= node.val:
                    return False
                elif level % 2 == 1 and level_to_vals[level] <= node.val:
                    return False
                level_to_vals[level] = node.val

            return traverse(node.left, level+1) and traverse(node.right, level+1)

        q = deque([root])
        print(q)
        return traverse(root, 0)
