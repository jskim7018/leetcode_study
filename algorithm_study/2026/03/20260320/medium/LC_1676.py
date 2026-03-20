class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # post traversal works.
        # return [count, ans]
        # if ans is not float('-inf') then just return ans
        # if it is then increase count if curr node val is in nodes

        nodes_st = set()
        for node in nodes:
            nodes_st.add(node.val)

        def post_traversal(node: 'TreeNode') -> list:
            if node is None:
                return [0, None]

            left = post_traversal(node.left)
            right = post_traversal(node.right)

            ans = None
            if left[1] is not None:
                ans = left[1]
            elif right[1] is not None:
                ans = right[1]

            if ans is not None:
                return [-1, ans]
            else:
                cnt = left[0] + right[0]
                if node.val in nodes_st:
                    cnt += 1

                if cnt == len(nodes_st):
                    ans = node
                return [cnt, ans]

        return post_traversal(root)[1]
