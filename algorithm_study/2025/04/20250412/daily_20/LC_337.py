from typing import Optional
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def solve(node, can_take) -> int:
            if node == None:
                return 0

            left = solve(node.left, True)
            right = solve(node.right, True)
            not_take = left + right
            take = 0
            if can_take:
                left = solve(node.left, False)
                right = solve(node.right, False)
                take = left + right + node.val


            return max(not_take, take)

        return solve(root, True)
