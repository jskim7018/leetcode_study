from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth_totals = defaultdict(int)

        def traverse(node: Optional[TreeNode], depth: int):
            if node is None:
                return
            depth_totals[depth] += node.val

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)

        def traverse_solve(node: Optional[TreeNode], depth: int) -> int:
            if node is None:
                return 0
            left = traverse_solve(node.left, depth + 1)
            right = traverse_solve(node.right, depth + 1)
            if node.left is not None:
                node.left.val = depth_totals[depth+1] - (left+right)
            if node.right is not None:
                node.right.val = depth_totals[depth+1] - (left+right)
            return node.val

        root.val = 0
        traverse_solve(root, 0)

        return root
