class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            str_n = str(n)
            product = 1
            for c in str_n:
                product *= int(c)
            if product % t == 0:
                return n
            n += 1

        return n
