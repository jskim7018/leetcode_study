from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        n = len(arr)
        def is_valid_sequence(node: Optional[TreeNode], curr_idx: int) -> bool:
            if node is None:
                return False
            if curr_idx >= n:
                return False

            is_leaf = node.left is None and node.right is None
            if arr[curr_idx] == node.val:
                if curr_idx == n-1:
                    if is_leaf:
                        return True
                    else:
                        return False
                else:
                    return (is_valid_sequence(node.left, curr_idx+1)
                            or is_valid_sequence(node.right, curr_idx + 1))
            else:
                return False

        return is_valid_sequence(root, 0)
