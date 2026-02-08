from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal ans

            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            if abs(left-right) > 1:
                ans = False

            return max(left, right) + 1

        traverse(root)

        return ans
