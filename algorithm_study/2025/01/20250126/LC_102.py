from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_values = {}

        def traverse(node: Optional[TreeNode], curr_level: int):
            if node is None:
                return

            if curr_level not in level_values:
                level_values[curr_level] = []

            level_values[curr_level].append(node.val)
            traverse(node.left, curr_level+1)
            traverse(node.right, curr_level+1)

        traverse(root, 0)
        return list(level_values.values())