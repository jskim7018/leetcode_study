class Fenwick:
    """1-indexed Fenwick Tree for point updates and prefix sums."""
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n+1)

    def update(self, i, v):
        # add v at index i (1 ≤ i ≤ n)
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def query(self, i):
        # sum of [1..i]
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
