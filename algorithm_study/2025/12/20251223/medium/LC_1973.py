from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal ans

            if node is None:
                return 0

            sum_of_descendants = traverse(node.left) + traverse(node.right)
            if node.val == sum_of_descendants:
                ans += 1

            return sum_of_descendants + node.val

        traverse(root)

        return ans
