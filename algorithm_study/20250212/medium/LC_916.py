from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter2 = Counter()

        for word in words2:
            counter = Counter(word)
            for c in counter.items():
                if c[0] in counter2:
                    counter2[c[0]] = max(counter2[c[0]], c[1])
                else:
                    counter2[c[0]] = c[1]

        universal_words = []
        for word in words1:
            counter = Counter(word)
            if counter2 <= counter:
                universal_words.append(word)

        return universal_words
