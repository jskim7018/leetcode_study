from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        for q in queries:
            for word in dictionary:
                diff = 0
                for q_w, d_w in zip(q,word):
                    if q_w != d_w:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2:
                    ans.append(q)
                    break

        return ans
