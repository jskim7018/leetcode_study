from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        nodes_left = []
        nodes_right = []
        def traverse_left(node: Optional[TreeNode], nodes):
            if node is None:
                return
            nodes.append(node.val)
            nodes.append("1")
            traverse_left(node.left, nodes)
            nodes.append("2")
            traverse_left(node.right, nodes)

        def traverse_right(node: Optional[TreeNode], nodes):
            if node is None:
                return
            nodes.append(node.val)
            nodes.append("1")
            traverse_right(node.right, nodes)
            nodes.append("2")
            traverse_right(node.left, nodes)

        traverse_left(root.left, nodes_left)
        traverse_right(root.right, nodes_right)

        print(nodes_left)
        print(nodes_right)
        return nodes_left == nodes_right