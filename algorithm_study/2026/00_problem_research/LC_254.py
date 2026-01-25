from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        ans = []
        for i in range(2, int(n**0.5)+1):
            curr_div = i
            tmp_n = n
            tmp = []
            while curr_div <= tmp_n:
                if tmp_n % curr_div == 0 and tmp_n//curr_div >= curr_div:
                    tmp.append(curr_div)
                    tmp_n = tmp_n//curr_div
                    ans.append(tmp + [tmp_n])
                else:
                    curr_div += 1

        return ans
