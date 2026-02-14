from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # x는 최대 3개의 영역이 있음. y는 결국 3개의 영역중 하나를 가져 가는 것
        # y가 제일 큰것을 가져가는게 좋은데 만약 나머지가 적으면 이기는 것.
        x_left_subtree_cnt = 0
        x_right_subtree_cnt = 0
        no_x_subtree_cnt = 0

        # TODO: parent는 그냥 x의 children의 합 + 1을 전체에서 빼면 되는 것임.
        def inorder_traverse(node: Optional[TreeNode], is_x_subtree:bool) -> int:
            nonlocal x_left_subtree_cnt
            nonlocal x_right_subtree_cnt
            nonlocal no_x_subtree_cnt

            if node is None:
                return 0

            if node.val == x:
                is_x_subtree = True

            left_subtree_sum = inorder_traverse(node.left, is_x_subtree)
            right_subtree_sum = inorder_traverse(node.right, is_x_subtree)

            if node.val == x:
                x_left_subtree_cnt = left_subtree_sum
                x_right_subtree_cnt = right_subtree_sum
            if not is_x_subtree:
                no_x_subtree_cnt += 1

            if is_x_subtree:
                return left_subtree_sum + right_subtree_sum + 1
            else:
                return 0

        inorder_traverse(root, False)

        lst = [no_x_subtree_cnt, x_left_subtree_cnt, x_right_subtree_cnt]
        lst.sort()

        if lst[2] > sum(lst[:2])+1:
            return True
        else:
            return False
