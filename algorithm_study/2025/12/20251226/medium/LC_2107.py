from typing import List
from collections import Counter


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)

        counter = Counter(candies)

        for i in range(k):
            counter[candies[i]] -= 1
            if counter[candies[i]] == 0:
                del counter[candies[i]]

        ans = len(counter)
        for i in range(k, n):
            counter[candies[i]] -= 1
            if counter[candies[i]] == 0:
                del counter[candies[i]]
            counter[candies[i - k]] += 1
            ans = max(ans, len(counter))

        return ans
