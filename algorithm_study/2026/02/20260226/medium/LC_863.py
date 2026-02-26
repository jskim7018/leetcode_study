from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # could create a graph and do bfs.
        # but is there one pass solution?
        # target의 children은 쉽게 구할 수 있음.
        def traverse_from_root(node: TreeNode, depth: int):
            if node is None:
                return {}

            if node == target:
                return depth

            left = traverse_from_root(node.left, depth + 1)
            right = traverse_from_root(node.right, depth + 1)

            ret = {depth: [node.val]}

            if isinstance(left, int):
                need_depth = depth + k - (left - depth)
                if need_depth in right:
                    ans.extend(right[need_depth])
                if need_depth in ret:
                    ans.extend(ret[need_depth])
                return left
            elif isinstance(right, int):
                need_depth = depth + k - (right - depth)
                if need_depth in left:
                    ans.extend(left[need_depth])
                if need_depth in ret:
                    ans.extend(ret[need_depth])
                return right

            for key, v in right.items():
                if key in ret:
                    ret[key].extend(v)
                else:
                    ret[key] = v
            for key, v in left.items():
                if key in ret:
                    ret[key].extend(v)
                else:
                    ret[key] = v

            return ret

        def traverse_from_target(node: TreeNode, depth: int):
            if node is None:
                return

            if depth == k:
                ans.append(node.val)
                return

            traverse_from_target(node.left, depth + 1)
            traverse_from_target(node.right, depth + 1)

        ans = []

        traverse_from_root(root, 0)
        traverse_from_target(target, 0)
        return ans
