from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def bfs():
            q = deque()
            q.append(root)

            ans = 0
            while q:
                curr_nodes = deque()
                node_vals = []
                idx = 0
                while q:
                    node = q.popleft()
                    node_vals.append([node.val,idx])
                    curr_nodes.append(node)
                    idx += 1

                sorted_node_vals = sorted(node_vals)

                for i in range(len(node_vals)):
                    if sorted_node_vals[i][0] != node_vals[i][0]:
                        node_vals[i], node_vals[sorted_node_vals[i][1]] \
                            = node_vals[sorted_node_vals[i][1]], node_vals[i]
                        node_vals[sorted_node_vals[i][1]][1] = sorted_node_vals[i][1]
                        ans += 1

                for node in curr_nodes:
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
            return ans

        return bfs()
