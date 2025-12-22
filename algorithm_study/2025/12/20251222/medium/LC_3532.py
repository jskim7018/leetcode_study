from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int],
                             maxDiff: int, queries: List[List[int]]) -> List[bool]:

        unionFind = UnionFind(n)
        for i in range(1,n):
            if nums[i]-nums[i-1] <= maxDiff:
                unionFind.union(i, i-1)
            else:
                continue

        ans = []
        for q in queries:
            ans.append(unionFind.find(q[0]) == unionFind.find(q[1]))

        return ans

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True
