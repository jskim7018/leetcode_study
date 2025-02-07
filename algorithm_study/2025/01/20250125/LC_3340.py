class Solution:
    def isBalanced(self, num: str) -> bool:
        num_list = [int(x) for x in num]

        sum_even = 0
        sum_odd = 0

        for i, v in enumerate(num_list):
            if i%2 == 0:
                sum_even += v
            else:
                sum_odd += v

        return sum_even == sum_odd
