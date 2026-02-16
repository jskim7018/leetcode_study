class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        i = 0
        while i < 32:
            bit = n % 2
            ans = (ans << 1) | bit
            i += 1
            n //= 2

        return ans
