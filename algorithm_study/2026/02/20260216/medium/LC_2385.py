from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # graph/tree 자료구조로 정의하고 bfs를 돌리면 쉽게 해결 가능.
        # 따로 안만들고 풀기. child 각각의 거리를 구함. child의 subtree안에 start가 있다면 start 까지 거리만 반환.
        # start 부터 별도로 아래 child 가장 큰 것 구함.
        # TODO: is_start flag를 안쓰고 음수를 반환해서 음수가 나오면 abs(val)이 start까지의 거리로 볼 수 있음.
        ans = 0

        def traverse(node: Optional[TreeNode]) -> list:  # [is_start, dist]
            nonlocal ans

            if node is None:
                return [False, 0]

            left = traverse(node.left)
            right = traverse(node.right)

            is_start = False
            if node.val == start:
                is_start = True
            if left[0] or right[0]:
                ans = max(ans, left[1] + right[1])
                if left[0]:
                    dist = left[1]
                else:
                    dist = right[1]
            else:
                dist = max(left[1], right[1])
            if is_start:
                ans = max(ans, dist)
                dist = 0

            return [left[0] or right[0] or is_start, dist + 1]

        traverse(root)
        return ans
