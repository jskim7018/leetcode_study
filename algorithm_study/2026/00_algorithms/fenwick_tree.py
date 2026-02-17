class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, i, delta):
        """Add delta to index i (1-based index)."""
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        """Return prefix sum from 1 to i (inclusive)."""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, left, right):
        """Return sum from left to right (1-based index)."""
        return self.query(right) - self.query(left - 1)