from collections import Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())

        st = set()
        for k, v in counter.items():
            if v == max_freq:
                st.add(k)

        ans = []
        for i in range(len(s)-1, -1, -1):
            if s[i] in st:
                ans.append(s[i])
                st.remove(s[i])

        ans.reverse()

        return ''.join(ans)
