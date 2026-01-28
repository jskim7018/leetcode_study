from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.count -= 1
        return True

    def component_size(self, x):
        return self.size[self.find(x)]

    def components(self):
        return self.count


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Union find or dfs. both 가능.
        union_find = UnionFind(n)

        for e in edges:
            union_find.union(e[0], e[1])

        ans = 0
        visited = set()
        for i in range(n):
            x = union_find.find(i)
            if x not in visited:
                size = union_find.size[x]
                ans += size * (n-size)
                visited.add(x)

        return ans//2
