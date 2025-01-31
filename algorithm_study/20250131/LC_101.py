from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check_valid(node1, node2) -> bool:
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            ret = (check_valid(node1.left, node2.right)
                   and check_valid(node1.right, node2.left))

            return ret

        return check_valid(root.left, root.right)