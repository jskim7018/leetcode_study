import pytest
import math
from collections import defaultdict


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        _sum_digit_fact = 0
        counter = defaultdict(int)

        while n > 0:
            digit = n % 10
            counter[digit] += 1
            _sum_digit_fact += math.factorial(digit)
            n //= 10

        counter_sum = defaultdict(int)
        while _sum_digit_fact > 0:
            digit = _sum_digit_fact % 10
            counter_sum[digit] += 1
            _sum_digit_fact //= 10

        if len(counter) == len(counter_sum):
            for k in counter.keys():
                if counter[k] != counter_sum[k]:
                    return False
            return True
        else:
            return False


@pytest.mark.parametrize("n_input, expected", [
    (145, True),
    (10, False),
    (1, True),
    (3, False)
])
def test_isDigitorialPermutation(n_input, expected):
    sol = Solution()
    assert sol.isDigitorialPermutation(n_input) == expected
