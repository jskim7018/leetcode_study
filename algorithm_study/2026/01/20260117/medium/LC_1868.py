from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        en1_n = len(encoded1)
        en2_n = len(encoded2)

        en1_idx = 0
        en2_idx = 0

        ans = []
        prev_prod_num = -1
        prev_freq = 0
        while en1_idx < en1_n and en2_idx < en2_n:
            en1_num = encoded1[en1_idx][0]
            en1_freq = encoded1[en1_idx][1]

            en2_num = encoded2[en2_idx][0]
            en2_freq = encoded2[en2_idx][1]

            if en1_freq > en2_freq:
                freq = en2_freq
                encoded1[en1_idx][1] -= en2_freq
                en2_idx += 1
            elif en1_freq < en2_freq:
                freq = en1_freq
                encoded2[en2_idx][1] -= en1_freq
                en1_idx += 1
            else:
                freq = en1_freq
                en2_idx += 1
                en1_idx += 1

            prod_num = en1_num * en2_num
            if prod_num != prev_prod_num:
                if prev_prod_num != -1:
                    ans.append([prev_prod_num, prev_freq])
                prev_prod_num = prod_num
                prev_freq = freq
            else:
                prev_freq += freq

            if en1_idx >= en1_n or en2_idx >= en2_n:
                ans.append([prev_prod_num, prev_freq])

        return ans
