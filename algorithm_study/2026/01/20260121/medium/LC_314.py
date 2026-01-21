from typing import Optional, List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        v_to_vals = defaultdict(list)
        min_v = 0
        max_v = 0

        def bfs():
            nonlocal min_v
            nonlocal max_v
            q = deque()
            q.append((root, 0))

            while q:
                node, v = q.popleft()

                if node is None:
                    continue

                min_v = min(min_v, v)
                max_v = max(max_v, v)

                v_to_vals[v].append(node.val)

                q.append((node.left, v-1))
                q.append((node.right, v+1))

        bfs()

        ans = []
        for i in range(min_v, max_v + 1):
            if len(v_to_vals[i]) > 0:
                ans.append(v_to_vals[i])

        return ans
