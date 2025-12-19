from functools import reduce
import operator


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = []

        tmp_n = n
        while tmp_n > 0:
            digits.append(tmp_n%10)
            tmp_n //= 10

        _sum = sum(digits)
        _prod = reduce(operator.mul, digits, 1)

        if n % (_sum + _prod) == 0:
            return True
        else:
            return False
