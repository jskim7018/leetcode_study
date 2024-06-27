from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left_value_seq1 = []
        left_value_seq2 = []
        self.dfs(root1, left_value_seq1)
        self.dfs(root2, left_value_seq2)

        return left_value_seq1 == left_value_seq2

    def dfs(self, root: Optional[TreeNode], left_value_seq: List[int]):
        if root is None:
            return
        if root.left is None and root.right is None:
            left_value_seq.append(root.val)
            return

        self.dfs(root.left, left_value_seq)
        self.dfs(root.right, left_value_seq)
