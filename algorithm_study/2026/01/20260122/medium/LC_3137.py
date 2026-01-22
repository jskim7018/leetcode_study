from collections import defaultdict


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        counter = defaultdict(int)

        n = len(word)

        max_freq = 0
        for i in range(0, n, k):
            counter[word[i:i+k]] += 1
            if max_freq < counter[word[i:i+k]]:
                max_freq = counter[word[i:i+k]]

        return n//k - max_freq
