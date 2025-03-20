# TODO: Check and Study
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX  # Attach one root to another
            return True
        return False