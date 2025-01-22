from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: Optional[TreeNode], currSum: int) -> bool:
            if node is None:
                return False

            currSum += node.val

            if node.left is None and node.right is None:
                return currSum == targetSum

            else:
                return dfs(node.left, currSum) | dfs(node.right, currSum)

        return dfs(root, 0)
