
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = []
        q_ancestors = set()

        while p:
            p_ancestors.append(p)
            p = p.parent
        while q:
            q_ancestors.add(q.val)
            q = q.parent

        for p_a in p_ancestors:
            if p_a.val in q_ancestors:
                return p_a

        return p


