from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        binary_st_sizes = []
        # TODO: perfect tree 특성. 왼쪽, 오른쪽 child 모두 같은 사이즈의 perfect tree.
        # TODO: 그러므로 depth를 굳이 구하지 않아도 됨. saves space and time.
        def post_order_traversal(node:Optional[TreeNode], depth: int) -> List[int]:
            if node is None:
                return [0, depth-1]

            left = post_order_traversal(node.left, depth+1)
            right = post_order_traversal(node.right, depth+1)

            subtree_node_cnt = left[0] + right[0] + 1
            max_depth = max(left[1], right[1])
            depth_from_curr = max_depth - depth

            need_cnt = (1 << (depth_from_curr+1))-1

            if need_cnt == subtree_node_cnt:
                binary_st_sizes.append(subtree_node_cnt)

            return [subtree_node_cnt, max_depth]


        post_order_traversal(root, 0)

        binary_st_sizes.sort(reverse=True)
        if k-1 < len(binary_st_sizes):
            return binary_st_sizes[k-1]
        else:
            return -1
