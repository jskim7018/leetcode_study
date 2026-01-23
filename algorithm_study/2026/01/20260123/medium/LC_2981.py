from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        counter = defaultdict(int)

        curr = s[0]
        cnt = 1

        for i in range(1, n):
            if s[i] == curr:
                cnt += 1
            else:
                for j in range(1, cnt+1):
                    counter[(curr, j)] += cnt - j + 1
                cnt = 1
                curr = s[i]
        for j in range(1, cnt + 1):
            counter[(curr, j)] += cnt - j + 1
        maxim_len = -1
        for k, v in counter.items():
            if v >= 3 and k[1] > maxim_len:
                maxim_len = k[1]
        return maxim_len
