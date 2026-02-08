from collections import defaultdict


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # sliding window로 풀 수 있을듯.
        # sliding window right 끝까지 모두 가능.
        # 상수 시간 마저 optimize 해야 하는 문제.

        w2_counter = defaultdict(int)
        for w in word2:
            w2_counter[w] += 1
        n = len(word1)
        l = 0
        w1_counter = defaultdict(int)
        ans = 0
        need = len(w2_counter)

        start = 0
        curr_need = need
        for i in range(n):
            w1_counter[word1[i]] += 1
            if w1_counter[word1[i]] == w2_counter[word1[i]]:
                curr_need -= 1
                if not curr_need:
                    w1_counter[word1[i]] -= 1
                    start = i
                    break
        if curr_need != 0:
            return 0

        need = ''
        for r in range(start, n):
            if word1[r] == need:
                need = ''
            w1_counter[word1[r]] += 1

            while need == '':
                ans += n - r
                w1_counter[word1[l]] -= 1
                if w1_counter[word1[l]] < w2_counter[word1[l]]:
                    need = word1[l]
                l += 1
        return ans
