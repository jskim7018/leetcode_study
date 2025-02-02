from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def traverse(node: Optional[TreeNode], curr_val:str):
            nonlocal ans
            if node is None:
                return


            if node.left is None and node.right is None:
                ans += int(curr_val+str(node.val))

            traverse(node.left, curr_val+str(node.val))
            traverse(node.right, curr_val+str(node.val))

        traverse(root, "")
        return ans
