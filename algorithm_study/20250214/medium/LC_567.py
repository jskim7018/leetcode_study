from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        counter_s1 = Counter(s1)
        counter_s2 = Counter()

        for r, c in enumerate(s2):
            counter_s2[c] += 1
            while l <= r and counter_s2[c] > counter_s1[c]:
                counter_s2[s2[l]] -= 1
                if counter_s2[s2[l]] == 0:
                    del counter_s2[s2[l]]
                l += 1
            if counter_s2 == counter_s1:
                return True

        return False
