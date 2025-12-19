from collections import Counter


class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        counter = Counter(s)

        keep_st = set()

        for v, f in counter.items():
            if f < k:
                keep_st.add(v)

        ans = ''
        for ch in s:
            if ch in keep_st:
                ans += ch

        return ans
