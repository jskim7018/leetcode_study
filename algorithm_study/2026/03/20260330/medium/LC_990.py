from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # union find.
        # 1. 일단 모든 == union find
        # 2. !=로 검증.

        not_equals = []
        union_find = UnionFind()

        for e in equations:
            a = e[0]
            b = e[3]

            if e[1] == '=':
                union_find.union(a,b)
            else:
                not_equals.append((a,b))

        for a, b in not_equals:
            if union_find.find(a) == union_find.find(b):
                return False

        return True
