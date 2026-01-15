from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        ans = 0
        def traverse(node: Optional[TreeNode]) -> int:
            nonlocal ans

            if not node:
                return -1

            dist1 = traverse(node.left)
            dist2 = traverse(node.right)

            if dist1 == -1 and dist2 == -1:
                if node.val == p or node.val == q:
                    return 1
                else:
                    return - 1

            if node.val == p or node.val == q:
                ans = max(dist1, dist2)
            else:
                if dist1 != -1 and dist2 != -1:
                    ans = dist1 + dist2
                else:
                    return max(dist1, dist2) + 1

            return -1

        traverse(root)

        return ans
