from typing import List
from collections import Counter


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)

        curr_alph_set = set()
        total_cnt = 0
        curr_cnt = 0
        ans = []
        for i, c in enumerate(s):
            if c not in curr_alph_set:
                total_cnt += counter[c]
                curr_alph_set.add(c)

            curr_cnt += 1
            if total_cnt == curr_cnt:
                ans.append(total_cnt)
                curr_cnt = 0
                total_cnt = 0

        return ans
