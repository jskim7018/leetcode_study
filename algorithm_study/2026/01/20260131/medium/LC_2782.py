from typing import Optional


# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
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

class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        union_find = UnionFind(n)
        for i in range(n):
            if union_find.find(i) >= i:
                for j in range(i+1, n):
                    if categoryHandler.haveSameCategory(i, j):
                        union_find.union(i,j)

        st = set()
        for i in range(n):
            st.add(union_find.find(i))

        return len(st)
