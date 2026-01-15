from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = 0

        def traverse(node: Optional[TreeNode]) -> List[int,int]:
            nonlocal ans

            if not node:
                return [0, 0]

            left = traverse(node.left)
            right = traverse(node.right)

            left[0] += right[0] + 1
            left[1] += right[1]+node.val
            ans = max(ans, left[1] / left[0])

            return left

        traverse(root)

        return ans
