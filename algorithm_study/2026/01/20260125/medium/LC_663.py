from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:

        subtree_sums = set()

        def traverse(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            _sum = node.val
            _sum += traverse(node.left) + traverse(node.right)

            if node != root:
                subtree_sums.add(_sum)

            return _sum

        total_sum = traverse(root)
        if total_sum / 2 in subtree_sums:
            return True
        else:
            return False
