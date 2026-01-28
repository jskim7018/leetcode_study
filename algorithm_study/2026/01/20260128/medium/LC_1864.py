class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones_in_even = 0
        ones_in_odd = 0

        # TODO: 다른 방식으로는 메서드 하나 만들고 0으로 시작과 1로 시작을 그냥 다 해보는 것도 있음.
        for i in range(n):
            if s[i] == '1':
                if i % 2 == 0:
                    ones_in_even += 1
                else:
                    ones_in_odd += 1
        total_ones = ones_in_odd + ones_in_even
        total_zeroes = n - total_ones
        if len(s) % 2 == 0:
            if ones_in_odd + ones_in_even != n//2:
                return -1
            else:
                return n//2 - max(ones_in_even, ones_in_odd)
        else:
            if total_zeroes == total_ones + 1:
                return ones_in_even
            elif total_zeroes + 1 == total_ones:
                return ones_in_odd
            else:
                return -1
