class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        if s.count('1') == 1:
            return n-1
        else:
            last_one_idx = 0
            for i in range(n):
                if s[i] == '1':
                    last_one_idx = i

            middle_zeroes_cnt = 0
            for i in range(last_one_idx):
                if s[i] == '0':
                    middle_zeroes_cnt += 1
            return 1 + (middle_zeroes_cnt+1) + (n-1)
