from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 + 7
        ans = 0
        _sum = 0

        def sum_of_tree(node: Optional[TreeNode]) -> int:
            nonlocal ans

            if node is None:
                return 0
            curr_tree_sum = node.val + sum_of_tree(node.left) + sum_of_tree(node.right)

            ans = max(ans, (_sum - curr_tree_sum) * curr_tree_sum)
            return curr_tree_sum

        _sum = sum_of_tree(root)
        sum_of_tree(root)

        return ans % mod
