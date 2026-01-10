import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression + '+' # sentinel
        n = len(expression)

        numerators = []
        denominators = []

        is_pos = True
        is_numerator = True
        curr_num = []
        for i in range(n):
            if expression[i] == '+' or expression[i] == '-':
                if expression[i] == '+':
                    is_pos = True
                elif expression[i] == '-':
                    is_pos = False
                if not is_numerator:
                    denominators.append(int(''.join(curr_num)))
                    curr_num.clear()
                    is_numerator = True
            else:
                if expression[i].isdigit():
                    curr_num.append(expression[i])
                elif expression[i] == '/':
                    numerators.append(int(''.join(curr_num)))
                    if not is_pos:
                        numerators[-1] *= -1
                    curr_num.clear()
                    is_numerator = False

        lcm = math.lcm(*denominators)
        num_sum = 0
        for num, den in zip(numerators, denominators):
            mult = lcm//den
            num_sum += mult * num

        gcd = math.gcd(num_sum, lcm)
        num_sum //= gcd
        lcm //= gcd

        return str(num_sum) + '/' + str(lcm)
