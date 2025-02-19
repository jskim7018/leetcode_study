from typing import List
from collections import deque


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        st = set()
        ans_st = set()
        for i in range(10, n+1):
            curr = s[i-10:i]
            if curr in st:
                ans_st.add(curr)
            else:
                st.add(curr)
        return list(ans_st)
