from collections import Counter


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        s += ' '
        n = len(s)
        counter = Counter()
        start_c = s[0]
        cnt = 1
        for i in range(1, n):
            if (ord(start_c)-ord('a') + cnt) % 26 == ord(s[i]) - ord('a'):
                cnt += 1
            else:
                j = 0
                while j < cnt and j < 26:
                    key = (ord(start_c)-ord('a') + j) % 26
                    counter[key] = max(counter[key], cnt-j)
                    j += 1

                start_c = s[i]
                cnt = 1

        ans = 0
        for v in counter.values():
            ans += v

        return ans
