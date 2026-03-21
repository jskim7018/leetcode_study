from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(s: str) -> int:
            smallest = min(s)
            return s.count(smallest)

        # Step 1: count frequencies of words
        count = [0] * 12  # index 0~11 (we use 1~10)

        for w in words:
            count[f(w)] += 1

        # Step 2: build suffix sum
        # count[i] = number of words with frequency >= i
        for i in range(10, 0, -1):
            count[i] += count[i + 1]

        # Step 3: answer queries
        result = []
        for q in queries:
            fq = f(q)
            result.append(count[fq + 1])  # strictly greater

        return result