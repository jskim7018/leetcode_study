class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits = str(x)
        sum = 0
        for d in digits:
            sum += int(d)

        if x % sum == 0:
            return sum

        return -1
