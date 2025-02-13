from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        cnt = 0
        ans = []

        st = set()
        for i in range(n):
            if A[i] in st:
                cnt += 1
            else:
                st.add(A[i])

            if B[i] in st:
                cnt += 1
            else:
                st.add(B[i])
            ans.append(cnt)
        return ans