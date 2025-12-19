from typing import List, Optional


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        ans = []

        while root is not None:
            ans.append(root.val)
            root = root.next

        return ans
