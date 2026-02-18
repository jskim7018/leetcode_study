class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bef = n % 2
        n //= 2

        while n > 0:
            curr = n % 2
            if bef == curr:
                return False
            bef = curr
            n //= 2

        return True
