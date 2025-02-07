from collections import Counter


class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:

        counter_s = Counter()
        counter_t = Counter()

        split_size = len(s) // k

        for i in range(0,len(s), split_size):
            counter_s[s[i:i+split_size]] += 1
            counter_t[t[i:i+split_size]] += 1

        return counter_s == counter_t
