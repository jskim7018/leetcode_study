class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        st = set()

        n = len(s)
        # TODO: Rolling hash 자세히 공부 하기.
        ans = 0
        for i in range(n):
            for j in range(0, i+1):
                sub_str = s[j:i+1]
                if sub_str in st:
                    ans = max(ans, len(sub_str))
                else:
                    st.add(sub_str)

        return ans
