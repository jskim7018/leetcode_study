from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def tree_to_set(node: Optional[TreeNode], st):
            if node is None:
                return

            st.add(node.val)
            tree_to_set(node.left, st)
            tree_to_set(node.right, st)

        tree1_set = set()
        tree2_set = set()

        tree_to_set(root1, tree1_set)
        tree_to_set(root2, tree2_set)

        for e in tree1_set:
            opp = target-e
            if opp in tree2_set:
                return True

        return False
