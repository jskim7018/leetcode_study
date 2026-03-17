class Fancy:

    MOD = 10**9 + 7

    def __init__(self):
        self.arr = []
        self.a = 1
        self.b = 0

    def mod_inv(self, x):
        return pow(x, self.MOD - 2, self.MOD)

    def append(self, val: int) -> None:
        x = (val - self.b) % self.MOD
        x = x * self.mod_inv(self.a) % self.MOD
        self.arr.append(x)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = self.a * m % self.MOD
        self.b = self.b * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.a * self.arr[idx] + self.b) % self.MOD