from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 1

        def traverse_tree(node: Optional[TreeNode], prev, cnt):
            nonlocal ans

            if node is None:
                return

            if node.val == prev + 1:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
            prev = node.val

            traverse_tree(node.left, prev, cnt)
            traverse_tree(node.right, prev, cnt)

        traverse_tree(root.left, root.val, 1)
        traverse_tree(root.right, root.val, 1)

        return ans