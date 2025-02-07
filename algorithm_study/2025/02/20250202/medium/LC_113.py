from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []
        curr_path = []

        def traverse(node: Optional[TreeNode], curr_path):
            if node is None:
                return

            curr_path.append(node.val)
            if node.left is None and node.right is None:
                if sum(curr_path) == targetSum:
                    ans.append(list(curr_path))
                curr_path.pop()
                return

            traverse(node.left, curr_path)
            traverse(node.right, curr_path)
            curr_path.pop()

        traverse(root, curr_path)

        return ans
