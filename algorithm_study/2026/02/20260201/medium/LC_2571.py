class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        curr_zeroes = 0
        curr_ones = 0
        while n:
            bit = n % 2
            n //= 2

            if bit == 1:
                if curr_zeroes == 1 and curr_ones > 1:
                    ans += 1
                    curr_zeroes = 0
                curr_ones += 1
            else:
                if curr_zeroes == 0:
                    if curr_ones == 1:
                        ans += 1
                        curr_ones = 0
                    elif curr_ones > 1:
                        curr_zeroes += 1
                elif curr_zeroes >= 1:
                    if curr_ones > 1:
                        ans += 2
                    curr_zeroes = 0
                    curr_ones = 0

        if curr_ones == 1:
            ans += 1
        elif curr_ones > 1:
            ans += 2

        return ans

