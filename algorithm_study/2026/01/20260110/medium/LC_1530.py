from typing import Optional, List
from itertools import product


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        ans = 0

        def traverse(node: Optional[TreeNode]) -> Optional[List[int]]:
            nonlocal ans
            if node is None:
                return None

            if node.left is None and node.right is None:
                return [1]

            left = traverse(node.left)
            right = traverse(node.right)
            if left is None:
                return list([a+1 for a in right])
            elif right is None:
                return list([a+1 for a in left])
            
            ans += sum(
                1
                for a, b in product(left, right)
                if a + b <= distance
            )
            ret = left + right
            ret = [a+1 for a in ret]

            return list(ret)

        traverse(root)

        return ans
