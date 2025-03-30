from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        st = set(bank)

        def solve(currGene:str, mut_cnt:int) -> int:
            if currGene == endGene:
                return mut_cnt

            ret = float('inf')
            for b in st:
                cnt = 0
                for i in range(8):
                    if currGene[i] != b[i]:
                        cnt += 1
                if cnt == 1:
                    st.remove(b)
                    ret = min(ret, solve(b, mut_cnt+1))
                    st.add(b)

            return ret

        ans = solve(list(startGene),0)
        if ans == float('inf'):
            return -1
        else:
            return ans
