from typing import List
from collections import defaultdict


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        # Can do dfs per node (O(n^2)).
        # Is there faster/better way? If not why not?
        n = len(edges) + 1
        tree = defaultdict(list)
        for e in edges:
            tree[e[0]].append((e[1],e[2]))
            tree[e[1]].append((e[0],e[2]))

        def dfs(v: int, w_sum: int) -> int:
            ret = w_sum % signalSpeed == 0
            for u, w in tree[v]:
                if not visited[u]:
                    visited[u] = True
                    ret += dfs(u, w_sum + w)
            return ret

        ans = []
        for i in range(n):
            visited = [False] * n
            visited[i] = True
            signal_path_cnts = []
            for v, w in tree[i]:
                visited[v] = True
                signal_path_cnts.append(dfs(v, w))
            total_paths = sum(signal_path_cnts)
            ans_tmp = 0
            for j in range(len(signal_path_cnts)):
                ans_tmp += ((total_paths - signal_path_cnts[j]) * signal_path_cnts[j])
            ans.append(ans_tmp // 2)

        return ans
