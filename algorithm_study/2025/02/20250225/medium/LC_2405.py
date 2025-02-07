class Solution:
    def partitionString(self, s: str) -> int:
        st = set(s[0])
        ans = 1
        for c in s[1:]:
            if c in st:
                ans += 1
                st = set(c)
            else:
                st.add(c)
        return ans
