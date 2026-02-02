class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        def digit_sum(num: int) -> int:
            ret = 0
            while num:
                ret += num%10
                num //= 10
            return ret
        ans = 0
        i = 0
        while n:
            if digit_sum(n) <= target:
                return ans

            ans += (10-(n % 10)) * pow(10, i)

            n //= 10
            n += 1
            i += 1

        return -1
