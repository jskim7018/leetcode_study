import math


class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        K = int(math.log2(n)) + 1

        self.st = [[0] * n for _ in range(K)]
        self.st[0] = arr[:]

        for k in range(1, K):
            for i in range(n - (1 << k) + 1):
                self.st[k][i] = max(
                    self.st[k - 1][i],
                    self.st[k - 1][i + (1 << (k - 1))]
                )

    def query(self, l, r):
        k = int(math.log2(r - l + 1))
        return max(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )