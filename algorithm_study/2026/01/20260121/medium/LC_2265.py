from typing import Tuple
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def traverse(node: TreeNode) -> Tuple[int, int]:
            nonlocal ans

            if node is None:
                return 0, 0

            l_sum, l_cnt = traverse(node.left)
            r_sum, r_cnt = traverse(node.right)

            subtree_sum = l_sum + r_sum + node.val
            subtree_cnt = l_cnt + r_cnt + 1

            if node.val == math.floor(subtree_sum/subtree_cnt):
                ans += 1

            return subtree_sum, subtree_cnt

        traverse(root)

        return ans
