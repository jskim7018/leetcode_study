from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)

        odd_cnt = 0
        for c in counter.values():
            if c % 2 == 1:
                odd_cnt += 1

        if len(s) % 2 == 1:
            if odd_cnt <= 1:
                return True
            else:
                return False
        else:
            if odd_cnt == 0:
                return True
            else:
                return False
