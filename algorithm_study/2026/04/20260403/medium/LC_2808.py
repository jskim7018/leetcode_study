from typing import List
from collections import Counter


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        # 작은 것 부터 하는게 유리
        # even 갯수, odd 갯수, word 길이 모두 구함. (실제 알파벳 상관 없음.)
        # word 길이 작은 순으로 greedy 하게 만들어 나감.

        word_lens = []
        counter = Counter()
        for word in words:
            word_lens.append(len(word))
            counter.update(word)

        even_cnt = 0
        odd_cnt = 0
        for v in counter.values():
            even_cnt += v // 2
            odd_cnt += v % 2

        word_lens.sort()
        ans = 0
        for l in word_lens:
            need_evens = l // 2
            need_odds = l % 2

            if even_cnt >= need_evens:
                even_cnt -= need_evens
            else:
                break

            if odd_cnt >= need_odds:
                odd_cnt -= need_odds
            elif even_cnt > 0:
                even_cnt -= 1
                odd_cnt += 1
            else:
                break
            ans += 1

        return ans
