from typing import Optional
from collections import deque
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelMedian(self, root: Optional[TreeNode], level: int) -> int:

        def bfs() -> int:
            q = deque()
            q.append((root, 0))

            level_vals = []
            while q:
                node, curr_l = q.popleft()
                if node is None:
                    continue

                if level == curr_l:
                    level_vals.append(node.val)
                else:
                    q.append((node.left, curr_l + 1))
                    q.append((node.right, curr_l + 1))

            if len(level_vals):
                return level_vals[math.ceil(len(level_vals)//2)]
            else:
                return -1

        return bfs()
