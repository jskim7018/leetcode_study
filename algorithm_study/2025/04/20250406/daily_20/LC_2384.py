from collections import Counter, deque


class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(str(num))
        ans = deque()


        counter = [[k,v] for k,v in counter.items()]
        counter.sort()

        half = deque()
        for i in range(len(counter)):
            k = counter[i][0]
            v = counter[i][1]
            if v % 2 == 1:
                v -= 1
            for _ in range(v//2):
                half.appendleft(k)
            counter[i][1] -= (v//2) * 2

        maxim_center_key = -1
        for k, v in counter:
            if v > 0:
                if int(k) >= maxim_center_key:
                    maxim_center_key = int(k)
        ans += half
        if maxim_center_key != -1:
            ans += str(maxim_center_key)
        ans += reversed(half)
        ans = ''.join(ans).strip('0')

        if ans == '':
            return '0'
        else:
            return ans
