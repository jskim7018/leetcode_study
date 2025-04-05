from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        bin_to_range = dict()

        for i in range(len(s)):
            j = i
            while j < i+32 and j < len(s):
                bin_ = s[i:j+1]
                if bin_ not in bin_to_range:
                    bin_to_range[bin_] = [i,j]
                j += 1

        ans = []
        for q in queries:
            val = q[0] ^ q[1]
            bin_ = bin(val)[2:]
            if bin_ in bin_to_range:
                ans.append(bin_to_range[bin_])
            else:
                ans.append([-1, -1])

        return ans
