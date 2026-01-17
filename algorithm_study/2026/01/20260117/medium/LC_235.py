class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s = min(p.val, q.val)
        b = max(p.val, q.val)
        def getLCA(node: 'TreeNode', smaller: int, bigger: int) -> 'TreeNode':
            if node is None:
                return None

            ret = None
            curr = node.val
            if bigger < curr:
                ret = getLCA(node.left, smaller, bigger)
            elif smaller > curr:
                ret = getLCA(node.right, smaller, bigger)
            else:
                ret = node

            return ret

        return getLCA(root, s, b)
