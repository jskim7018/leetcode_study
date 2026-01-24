from typing import List
from itertools import product
from functools import cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        ops_set = set('+-*')

        @cache
        def dp(left: int, right: int) -> List[int]:
            if expression[left:right+1].isdigit():
                return [int(expression[left:right+1])]

            result = []
            for i in range(left, right + 1):
                if expression[i] in ops_set:
                    left_results = dp(left, i-1)
                    right_results = dp(i+1, right)
                    if expression[i] == '+':
                        result.extend([l+r for l, r in product(left_results, right_results)])
                    elif expression[i] == '-':
                        result.extend([l-r for l, r in product(left_results, right_results)])
                    elif expression[i] == '*':
                        result.extend([l*r for l, r in product(left_results, right_results)])
            return list(result)

        return dp(0, n-1)
