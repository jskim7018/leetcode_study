class Solution:
    def sumAndMultiply(self, n: int) -> int:

        non_zero_nums = []
        while n > 0:
            if n%10 != 0:
                non_zero_nums.append(n % 10)
            n //= 10
        non_zero_nums.reverse()
        non_zero_num = 0
        for num in non_zero_nums:
            non_zero_num *= 10
            non_zero_num += num

        _sum = sum(non_zero_nums)

        return non_zero_num * _sum
