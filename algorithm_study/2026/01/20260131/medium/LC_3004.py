from typing import List
from collections import defaultdict


class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        # post order traversal return [color, size]
        # if different from subtree then return [-1,-1]

        tree = defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        ans = 0
        def pos_order_traversal(node: int, parent: int) -> List[int]:
            nonlocal ans

            curr_color = colors[node]
            size = 1
            is_possible = True
            for nxt_node in tree[node]:
                if nxt_node != parent:
                    nxt = pos_order_traversal(nxt_node, node)
                    if nxt[0] != curr_color:
                        is_possible = False
                    else:
                        size += nxt[1]
            if is_possible:
                ans = max(ans, size)
                return [curr_color, size]
            else:
                return [-1, -1]

        pos_order_traversal(0, -1)

        return ans
