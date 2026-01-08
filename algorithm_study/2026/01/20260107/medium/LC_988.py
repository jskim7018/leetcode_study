from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        curr_str = []

        ans = None
        def traverse(node: Optional[TreeNode]):
            nonlocal ans
            if node is None:
                return
            curr_str.append(chr(node.val + ord('a')))
            if node.left is None and node.right is None:
                if ans is None:
                    ans = ''.join(curr_str[::-1])
                else:
                    ans = min(ans, ''.join(curr_str[::-1]))
            else:
                traverse(node.left)
                traverse(node.right)
            curr_str.pop()

        traverse(root)

        return ans
