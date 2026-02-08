from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def traverse(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False

            ret = check_sub_path(node, head)

            if ret:
                return ret
            else:
                ret = traverse(node.left) or traverse(node.right)
                return ret

        def check_sub_path(node: Optional[TreeNode], curr: Optional[ListNode]) -> bool:
            nonlocal head
            if curr is None:
                return True
            if node is None:
                return False

            if node.val == curr.val:
                return (check_sub_path(node.left, curr.next)
                        or check_sub_path(node.right, curr.next))
            else:
                return False

        return traverse(root)
