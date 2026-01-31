import copy
from typing import List


class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_alph_cnt = [[0] * 26 for _ in range(n)]

        for i in range(n):
            if i-1 >= 0:
                prefix_alph_cnt[i] = copy.deepcopy(prefix_alph_cnt[i-1])
            ch_int = ord(s[i]) - ord('a')
            prefix_alph_cnt[i][ch_int] += 1

        ans = []
        for q in queries:
            l, r = q
            curr_ans = 0
            for i in range(26):
                alph_cnt = prefix_alph_cnt[r][i]
                if l-1 >= 0:
                    alph_cnt -= prefix_alph_cnt[l-1][i]
                curr_ans += ((alph_cnt+1)*alph_cnt) // 2
            ans.append(curr_ans)

        return ans
