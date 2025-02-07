from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        nums = deque()
        def traverse(node:Optional[TreeNode]) -> int:
            if node is None:
                return float('inf')

            ret = traverse(node.left)
            nums.append(node.val)
            if len(nums) > 2:
                nums.popleft()
            if len(nums) == 2:
                ret = min(ret, abs(nums[0]-nums[1]))
            ret = min(ret, traverse(node.right))

            return ret

        return traverse(root)
