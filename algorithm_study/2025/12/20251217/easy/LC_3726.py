class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0

        pow = 0
        while n > 0:
            if n % 10:
                ans += (n % 10) * (10 ** pow)
                pow += 1
            n //= 10

        return ans

# 아래 방법도 가능함.
# class Solution:
#     def removeZeros(self, n: int) -> int:
#         return int(str(n).replace('0', ''))
