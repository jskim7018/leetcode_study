from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 1, 0)-1

    def dfs(self, node:Optional[TreeNode], cnt: int, bef: int) -> int:
        if node is None:
            return 0

        ret = cnt
        if bef == 1:
            ret = max(ret, self.dfs(node.left, 2, 1))
        else:
            ret = max(ret, self.dfs(node.left, cnt + 1, 1))

        if bef == 2:
            ret = max(ret, self.dfs(node.right, 2, 2))
        else:
            ret = max(ret, self.dfs(node.right, cnt + 1, 2))
        return ret
