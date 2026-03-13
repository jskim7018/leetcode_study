from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:

        self.ans_dist = float('inf')
        self.ans_leaf = None

        def dfs(node):
            if not node:
                return (-1, float('inf'), None)

            if not node.left and not node.right:
                dist_k = 0 if node.val == k else -1
                if node.val == k:
                    self.ans_dist = 0
                    self.ans_leaf = node.val
                return (dist_k, 0, node.val)

            lk, ld, lv = dfs(node.left)
            rk, rd, rv = dfs(node.right)

            if ld <= rd:
                leaf_dist = ld + 1
                leaf_val = lv
            else:
                leaf_dist = rd + 1
                leaf_val = rv

            dist_k = -1
            if node.val == k:
                dist_k = 0
                if leaf_dist < self.ans_dist:
                    self.ans_dist = leaf_dist
                    self.ans_leaf = leaf_val
            elif lk != -1:
                dist_k = lk + 1
                candidate = dist_k + 1 + rd
                if rv is not None and candidate < self.ans_dist:
                    self.ans_dist = candidate
                    self.ans_leaf = rv
            elif rk != -1:
                dist_k = rk + 1
                candidate = dist_k + 1 + ld
                if lv is not None and candidate < self.ans_dist:
                    self.ans_dist = candidate
                    self.ans_leaf = lv

            return (dist_k, leaf_dist, leaf_val)

        dfs(root)
        return self.ans_leaf
