class RollingHash:
    def __init__(self, s: str):
        self.mod = 10**9 + 7
        self.base = 91138233   # any large random odd number
        n = len(s)

        self.h = [0] * (n + 1)
        self.p = [1] * (n + 1)

        for i in range(n):
            self.h[i + 1] = (self.h[i] * self.base + ord(s[i])) % self.mod
            self.p[i + 1] = (self.p[i] * self.base) % self.mod

    def get(self, l: int, r: int) -> int:
        # returns hash of s[l:r]
        return (self.h[r] - self.h[l] * self.p[r - l]) % self.mod

# TODO: probability of collision in rolling hash???