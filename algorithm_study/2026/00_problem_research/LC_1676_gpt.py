# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        target = set(nodes)

        def dfs(node):
            if not node:
                return None

            # If current node is one of the targets
            if node in target:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            # If both sides found something → this is LCA
            if left and right:
                return node

            return left if left else right

        return dfs(root)