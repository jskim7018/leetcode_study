from typing import List
import heapq
import pytest


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(0,n))
        self.rank = [0] * n

    def find(self, a) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b) -> bool:
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return False

        if self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root
        elif self.rank[a_root] < self.rank[b_root]:
            self.parent[a_root] = b_root
        else:
            self.parent[b_root] = a_root
            self.rank[a_root] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST problem: Prim, Kruskal 가능
        # TODO: Prim is better for this problem since no need to compute all edges with Prim.
        def manhattan_dist(c1, c2) -> int:
            return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

        edges_heap = []
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                edges_heap.append((manhattan_dist(points[i], points[j]), i, j))

        heapq.heapify(edges_heap)
        uf = UnionFind(n)

        ans = 0
        cnt = 0
        while edges_heap:
            w, v, u = heapq.heappop(edges_heap)

            if uf.find(v) == uf.find(u):
                continue
            uf.union(v, u)
            cnt += 1
            ans += w

            if cnt == n-1:
                break

        return ans


@pytest.mark.parametrize("input_points, expected", [
    ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
    ([[3,12],[-2,5],[-4,1]], 18)
])
def test_minCostConnectPoints(input_points, expected):
    sol = Solution()

    assert sol.minCostConnectPoints(input_points) == expected
