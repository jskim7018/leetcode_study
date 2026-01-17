from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        c_to_val = {c: v for c, v in zip(chars, vals)}
        for alph in range(0, 26):
            ch_alph = chr(alph + ord('a'))
            if ch_alph not in c_to_val:
                c_to_val[ch_alph] = alph + 1

        ans = 0

        curr = 0
        for ch in s:
            curr += c_to_val[ch]
            if curr < 0:
                curr = 0
            ans = max(ans, curr)

        return ans
