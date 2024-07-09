from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.p_parents = []
        self.q_parents = []


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = []
        self.get_parents(root, p, q, parents)

        q_set = set(self.q_parents)

        for v in reversed(self.p_parents):
            if v in q_set:
                return TreeNode(v)


    def get_parents(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', parents:List):
        if root is None:
            return

        parents.append(root.val)
        if root.val is p.val:
            self.p_parents = parents.copy()
        if root.val is q.val:
            self.q_parents = parents.copy()
        self.get_parents(root.left, p, q, parents)
        self.get_parents(root.right, p, q, parents)
        parents.pop()
