from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = Counter(s)

        odd_chr = ''
        for k,v in counter.items():
            if v%2==1:
                counter[k]-=1
                odd_chr = k
            counter[k] //=2

        lst = list(counter.items())
        lst.sort()

        ans = []
        for alph, cnt in lst:
            for _ in range(cnt):
                ans.append(alph)

        if odd_chr != '':
            ans.append(odd_chr)

        ans += ans[:len(ans) - (odd_chr != '')][::-1]

        return ''.join(ans)
