from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n: int):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x: int) -> int:
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x: int, y: int) -> bool:
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return False

                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_y] = root_x
                    self.rank[root_x] += 1

                return True

        n = len(stones)

        union_find = UnionFind(n)

        same_row_stones = defaultdict(list)
        same_col_stones = defaultdict(list)
        for i in range(n):
            same_row_stones[stones[i][0]].append(i)
            same_col_stones[stones[i][1]].append(i)

        for stones in same_row_stones.values():
            first = stones[0]
            for s in stones:
                union_find.union(first, s)
        for stones in same_col_stones.values():
            first = stones[0]
            for s in stones:
                union_find.union(first, s)

        st = set()
        for i in range(n):
            st.add(union_find.find(i))

        return n - len(st)
