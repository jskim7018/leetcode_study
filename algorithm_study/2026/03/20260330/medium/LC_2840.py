from collections import defaultdict


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # index 짝수끼리, 홀수끼리만 교환 가능.
        counter_even = defaultdict(int)
        counter_odd = defaultdict(int)

        n = len(s1)

        for i in range(n):
            if i % 2 == 0:
                counter_even[s1[i]] += 1
                counter_even[s2[i]] -= 1
            else:
                counter_odd[s1[i]] += 1
                counter_odd[s2[i]] -= 1

        for v in counter_even.values():
            if v != 0:
                return False
        for v in counter_odd.values():
            if v != 0:
                return False

        return True
