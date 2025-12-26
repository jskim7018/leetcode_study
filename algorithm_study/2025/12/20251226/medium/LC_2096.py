from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        start_path = deque()
        dest_path = deque()
        is_start_found = 0
        is_dest_found = 0
        def traverse(node: Optional[TreeNode]):
            nonlocal is_start_found
            nonlocal is_dest_found

            if node is None:
                return
            if node.val == startValue:
                is_start_found = 1 + is_dest_found
            if node.val == destValue:
                is_dest_found = 1 + is_start_found

            if not is_start_found:
                start_path.append('L')
            if not is_dest_found:
                dest_path.append('L')
            traverse(node.left)
            if not is_start_found:
                start_path.pop()
            if not is_dest_found:
                dest_path.pop()

            if not is_start_found:
                start_path.append('R')
            if not is_dest_found:
                dest_path.append('R')
            traverse(node.right)
            if not is_start_found:
                start_path.pop()
            if not is_dest_found:
                dest_path.pop()

        traverse(root)
        while start_path and dest_path:
            if start_path[0] == dest_path[0]:
                start_path.popleft()
                dest_path.popleft()
            else:
                break
        ans = []
        for p in start_path:
            ans.append('U')
        for p in dest_path:
            ans.append(p)

        return ''.join(ans)
