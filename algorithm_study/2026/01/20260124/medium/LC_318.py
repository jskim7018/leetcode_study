from typing import List
from collections import defaultdict


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_to_bit_masks = defaultdict(int)
        for word in words:
            if word not in word_to_bit_masks:
                bit_mask = 0
                for ch in word:
                    bit_pos = ord(ch) - ord('a')
                    bit_mask = bit_mask | 1 << bit_pos
                word_to_bit_masks[word] = bit_mask
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                w1 = words[i]
                w2 = words[j]

                if word_to_bit_masks[w1] & word_to_bit_masks[w2] == 0:
                    ans = max(ans, len(w1) * len(w2))
        return ans
