from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 1)
    def dfs(self, root: Optional[TreeNode], depth) -> int:
        if root is None:
            return 0

        return max(depth,
                   self.dfs(root.left, depth+1),
                   self.dfs(root.right, depth+1))
