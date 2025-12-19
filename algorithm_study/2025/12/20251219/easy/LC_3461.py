class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(digit) for digit in s]

        new_digits = []

        while len(digits) > 2:
            for i in range(len(digits)-1):
                new_digits.append((digits[i] + digits[i+1])%10)
            digits = list(new_digits)
            new_digits.clear()
            print(digits)

        return digits[0] == digits[1]

# class Solution:
#     def hasSameDigits(self, s: str) -> bool:
#         nums = list(map(int, s))
#
#         while len(nums) > 2:
#             nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
#
#         return nums[0] == nums[1]