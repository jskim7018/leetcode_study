from typing import List


class Solution:
    def permute(self, n: int) -> List[List[int]]:

        ans = []
        curr = []
        st = set()
        def alt_permute(idx, prev):
            if idx >= n:
                ans.append(list(curr))
                return

            for i in range(1, n+1):
                if i in st:
                    continue
                if prev != -1:
                    if prev % 2 != i % 2:
                        curr.append(i)
                        st.add(i)
                        alt_permute(idx+1, i)
                        curr.pop()
                        st.remove(i)
                else:
                    curr.append(i)
                    st.add(i)
                    alt_permute(idx+1, i)
                    curr.pop()
                    st.remove(i)

        alt_permute(0, -1)

        return ans
