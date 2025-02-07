from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        node_val_list = []
        def dfs(node: Optional[TreeNode], level):
            if node is None:
                return

            if len(node_val_list) <= level:
                node_val_list.append([])

            node_val_list[level].append(node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)

        avg_list = [sum(node_vals)/len(node_vals) for node_vals in node_val_list]

        return avg_list


