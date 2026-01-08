from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> TreeNode:

        def traverse_and_add(node: Optional[TreeNode], val: int, curr_depth: int):
            if node is None:
                return

            if curr_depth == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return

            traverse_and_add(node.left, val, curr_depth + 1)
            traverse_and_add(node.right, val, curr_depth + 1)

        if depth == 1:
            return TreeNode(val, root, None)
        else:
            traverse_and_add(root, val, 1)
            return root
