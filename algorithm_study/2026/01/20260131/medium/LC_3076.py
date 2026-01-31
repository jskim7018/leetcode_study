from typing import List
from collections import Counter


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        counter = Counter()
        for s in arr:
            seen = set()

            for i in range(len(s)):
                for j in range(i, len(s)):
                    seen.add(s[i:j+1])
            for se in seen:
                counter[se] += 1

        ans = []
        for idx, s in enumerate(arr):
            min_len = float('inf')
            substr = ''
            for i in range(len(s)):
                for j in range(i, len(s)):
                    cand_substr = s[i:j+1]
                    if counter[cand_substr] == 1:
                        if len(cand_substr) < min_len:
                            substr = cand_substr
                            min_len = len(cand_substr)
                        elif len(cand_substr) == min_len:
                            if cand_substr < substr:
                                substr = cand_substr
            ans.append(substr)
        return ans
