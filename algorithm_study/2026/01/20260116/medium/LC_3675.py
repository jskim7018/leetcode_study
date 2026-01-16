class Solution:
    def minOperations(self, s: str) -> int:
        st = set(s)
        if 'a' in st:
            st.remove('a')
        if len(st) == 0:
            return 0
        st.add('z')

        lst = list(st)

        lst.sort()

        ans = 0

        for i in range(1, len(lst)):
            ans += ord(lst[i]) - ord(lst[i - 1])

        return ans + 1