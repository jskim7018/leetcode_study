from typing import List
from collections import defaultdict


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        directed_edge_st = set([tuple(edge) for edge in edges])
        cnt_subtree_reverse = [0] * n

        def dfs_cnt_subtree_reverse(curr: int, parent: int) -> int:
            ret = 0
            for u in tree[curr]:
                if u == parent:
                    continue

                ret += dfs_cnt_subtree_reverse(u, curr)
                if (curr, u) not in directed_edge_st:
                    ret += 1
            cnt_subtree_reverse[curr] = ret
            return ret

        ans = [0] * n
        def dfs_solve(curr: int, parent: int, parent_sum: int):
            total = cnt_subtree_reverse[curr]

            ans[curr] = parent_sum + total

            for u in tree[curr]:
                if u == parent:
                    continue
                next_parent_sum = total - cnt_subtree_reverse[u] + parent_sum
                if (curr, u) not in directed_edge_st:
                    next_parent_sum -= 1
                if (u, curr) not in directed_edge_st:
                    next_parent_sum += 1
                dfs_solve(u, curr, next_parent_sum)

        dfs_cnt_subtree_reverse(0, -1)
        dfs_solve(0, -1, 0)

        return ans
