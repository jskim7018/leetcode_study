from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def sum_in_range(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            ret = 0
            if node.val >= low and node.val <= high:
                ret += node.val

            if node.val >= low:
                ret += sum_in_range(node.left)

            if node.val <= high:
                ret += sum_in_range(node.right)

            return ret

        return sum_in_range(root)
