from typing import List
from collections import defaultdict
import bisect


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # find for f(..) for all words and sort frequencies.
        # binary search on the sorted frequencies for each query

        def f(s: str) -> int:
            smallest = 'z'
            freqs = defaultdict(int)
            for ch in s:
                freqs[ch] += 1
                if ch < smallest:
                    smallest = ch

            return freqs[smallest]

        word_freqs = []
        for w in words:
            word_freqs.append(f(w))
        word_freqs.sort()

        n = len(word_freqs)
        ans = []
        for q in queries:
            q_freq = f(q)
            right_idx = bisect.bisect_right(word_freqs, q_freq)
            ans.append(n - right_idx)

        return ans
