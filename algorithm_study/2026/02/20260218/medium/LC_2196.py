from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        has_parent = set()
        nodes = dict()

        for desc in descriptions:
            parent, child, is_left = desc

            has_parent.add(child)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for node in nodes.values():
            if node.val not in has_parent:
                return node

        return None
