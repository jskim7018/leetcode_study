from typing import List
from collections import defaultdict, deque


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # start from leaves. (each leaf as group) (edge_cnt is zero)
        # bfs
        # if each group is divisible by k, then each are its own group. in-degree[parent] -= 1
        # else not divisible by k. add its sum to its parent then in-degree = zero
        # make next in degree zero to start then repeat.
        # TODO: Also can be solved with DFS. Try solving with dfs.
        tree = defaultdict(set)

        for e in edges:
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])

        def bfs() -> int:
            curr_node_sum = list(values)

            q = deque()
            visited = [False] * n

            for i in range(n):
                if len(tree[i]) <= 1:
                    q.append(i)
                    visited[i] = True

            ans = 0
            while q:
                next_q = deque()
                while q:
                    v = q.popleft()
                    if curr_node_sum[v] % k == 0:
                        ans += 1
                        curr_node_sum[v] = 0

                    for u in tree[v]:
                        curr_node_sum[u] += curr_node_sum[v]
                        tree[u].remove(v)
                        if not visited[u] and len(tree[u]) <= 1:
                            next_q.append(u)
                            visited[u] = True

                    tree[v].clear()
                q = next_q
            return ans

        return bfs()
