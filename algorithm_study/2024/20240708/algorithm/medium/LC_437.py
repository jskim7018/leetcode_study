from typing import Optional
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        return self.traverse(root, counter, 0, targetSum)

    def traverse(self, node: Optional[TreeNode],
                 parent_prefix_sum: Counter, last_prefix_sum:int,
                 targetSum: int) -> int:
        if node is None:
            return 0

        curr_prefix_sum = last_prefix_sum + node.val
        need = curr_prefix_sum - targetSum
        ret = parent_prefix_sum[need]
        parent_prefix_sum[curr_prefix_sum] += 1
        if targetSum == curr_prefix_sum:
            ret += 1
        ret += (self.traverse(node.left, parent_prefix_sum,
                                                  curr_prefix_sum, targetSum)
                + self.traverse(node.right, parent_prefix_sum,
                                                  curr_prefix_sum, targetSum))
        parent_prefix_sum[curr_prefix_sum] -= 1
        return ret
