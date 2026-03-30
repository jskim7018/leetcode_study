import math


class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10**9 + 7
        return (math.comb(n-1, k) * 2) % mod
