from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, words: List[str]) -> int:
        cnt_similar = defaultdict(int)

        for word in words:
            pivot = ord(word[0]) - ord('a')

            pivot_str = []
            for w in word:
                pivot_str.append(chr((26+ord(w)-ord('a')-pivot) % 26))

            cnt_similar[''.join(pivot_str)] += 1

        ans = 0
        for v in cnt_similar.values():
            ans += (v*(v-1))//2
        return ans
