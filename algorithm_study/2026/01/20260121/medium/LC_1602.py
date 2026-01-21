from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:

        u_depth = -1
        ans = None
        def traverse(node: TreeNode, depth: int):
            nonlocal u_depth
            nonlocal ans

            if node is None:
                return

            if u_depth == depth and ans is None:
                ans = node
                return
            elif node.val == u.val:
                u_depth = depth
                return

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)

        return ans
