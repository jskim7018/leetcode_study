from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        m = len(edges1) + 1
        n = len(edges2) + 1
        tree1 = [[] for _ in range(m)]
        tree2 = [[] for _ in range(n)]

        for e in edges1:
            tree1[e[0]].append(e[1])
            tree1[e[1]].append(e[0])
        for e in edges2:
            tree2[e[0]].append(e[1])
            tree2[e[1]].append(e[0])

        def count_target_nodes(curr: int, _k: int, curr_k: int, tree: List[List[int]],
                               visited: List[bool]) -> int:
            visited[curr] = True
            ret = 0
            if curr_k <= _k:
                ret += 1
            if curr_k > _k:
                return 0

            for nxt in tree[curr]:
                if not visited[nxt]:
                    ret += count_target_nodes(nxt, _k, curr_k+1, tree,visited)

            return ret

        tree2_maxim = 0
        for i in range(n):
            visited = [False]*n
            tree2_maxim = max(tree2_maxim, count_target_nodes(i, k-1,0, tree2, visited))

        ans = []
        for i in range(m):
            visited = [False] * m
            ans.append(count_target_nodes(i, k, 0, tree1, visited) + tree2_maxim)

        return ans
