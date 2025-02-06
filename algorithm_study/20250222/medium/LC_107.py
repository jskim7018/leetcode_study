from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []
        def traverse(node: Optional[TreeNode], depth: int):
            if node is None:
                return

            if len(ans) <= depth:
                ans.append([])
            ans[depth].append(node.val)

            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
        traverse(root, 0)

        return ans[::-1]
