class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10 ** 9 + 7

        ans = pow(pow(2, p) - 2, pow(2, p) // 2 - 1, mod) * (pow(2, p) - 1)
        ans %= mod

        return ans
