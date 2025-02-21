from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        k_frequent = list(counter.items())
        k_frequent.sort(key = lambda a: (-a[1], a[0]))
        ans = [a[0] for a in k_frequent[:k]]

        return ans