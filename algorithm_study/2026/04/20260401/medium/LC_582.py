from typing import List
from collections import defaultdict


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # simply build tree (directed edge)
        # then just do dfs
        tree = defaultdict(list)
        n = len(pid)

        for i in range(n):
            tree[ppid[i]].append(pid[i])

        ans = []

        def dfs(v: int) -> int:
            ans.append(v)
            for u in tree[v]:
                if u not in visited:
                    visited.add(u)
                    dfs(u)

        visited = set()
        visited.add(kill)
        dfs(kill)

        return ans
