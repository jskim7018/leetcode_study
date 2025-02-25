from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def check(node:Optional[TreeNode], leftBound, rightBound) -> bool:
            if node is None:
                return True
            if node.val <= leftBound or node.val >= rightBound:
                return False

            ret = check(node.left, leftBound, node.val) and check(node.right, node.val, rightBound)

            return ret

        return check(root, float('-inf'), float('inf'))