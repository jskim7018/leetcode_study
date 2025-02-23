from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(node: Optional[TreeNode], preorder: List[int], postorder: List[int]):
            node.val = preorder[0]
            if len(preorder) == 1:
                return

            child_preorder = preorder[1:]
            child_postorder = postorder[:-1]

            st_pre = set()
            st_post = set()

            i = 0
            while i < len(child_preorder):
                st_pre.add(child_preorder[i])
                st_post.add(child_postorder[i])
                if st_pre == st_post:
                    break
                i += 1

            node.left = TreeNode()
            build(node.left, child_preorder[:i+1], child_postorder[:i+1])
            if len(child_preorder[i+1:]) >= 1:
                node.right = TreeNode()
                build(node.right, child_preorder[i+1:], child_postorder[i+1:])

        root = TreeNode()
        build(root, preorder, postorder)

        return root