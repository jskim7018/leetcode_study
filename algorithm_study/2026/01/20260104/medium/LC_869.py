from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_str = str(n)
        counter = Counter(n_str)

        i = 0

        while True:
            pow2_str = str(2**i)
            pow2_digit_counter = Counter(pow2_str)

            if len(pow2_str) > len(n_str):
                break
            if counter == pow2_digit_counter:
                return True
            i += 1

        return False
