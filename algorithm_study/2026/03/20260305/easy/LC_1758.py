class Solution:
    def minOperations(self, s: str) -> int:
        zero_first = 0
        one_first = 0

        for i, ch in enumerate(s):
            if i % 2 == 0 and ch == '1' or i % 2 == 1 and ch == '0':
                zero_first += 1
            elif i % 2 == 0 and ch == '0' or i % 2 == 1 and ch == '1':
                one_first += 1

        return min(zero_first,one_first)
