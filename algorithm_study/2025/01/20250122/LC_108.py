from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildSortedTree(0, len(nums)-1, nums)

    def buildSortedTree(self, l: int, r: int, nums: List[int]) -> Optional[TreeNode]:
        if l > r:
            return None
        node = TreeNode()
        mid = (l + r) // 2
        node.val = nums[mid]
        node.left = self.buildSortedTree(l, mid - 1, nums)
        node.right = self.buildSortedTree(mid + 1, r, nums)

        return node
