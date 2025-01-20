from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Carry over if the digit is 9

        # If all digits were 9, the list becomes [0...0], so we add a leading 1
        return [1] + digits