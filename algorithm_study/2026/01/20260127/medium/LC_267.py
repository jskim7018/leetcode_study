from typing import List
from collections import Counter


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # odd는 최대 1개만 있어야 한다. 해당 odd 1개가 있으면 그 1개는 permutation에서 제외.
        # 중복인 애들도 permutation에서 고려.
        counter = Counter(s)

        odd_cnt = 0
        odd_letter = ''
        to_use = Counter()
        for k, v in counter.items():
            if v % 2 == 1:
                odd_cnt += 1
                odd_letter = k
                if odd_cnt > 1:
                    return []

            if v//2 != 0:
                to_use[k] = v//2

        ans = []
        curr = []
        def distinct_permutations():
            if not len(to_use):
                curr_str = ''.join(curr)
                rev_curr_str = curr_str[::-1]
                ans.append(curr_str + odd_letter + rev_curr_str)
                return

            keys = list(to_use.keys())

            for k in keys:
                to_use[k] -= 1
                curr.append(k)
                if to_use[k] == 0:
                    del to_use[k]
                distinct_permutations()
                curr.pop()
                to_use[k] += 1

        distinct_permutations()
        return ans