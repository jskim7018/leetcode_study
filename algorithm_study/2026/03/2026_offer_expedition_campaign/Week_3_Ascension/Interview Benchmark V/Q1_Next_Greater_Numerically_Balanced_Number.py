from typing import List
from functools import cache
from itertools import permutations


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        @cache
        def dp_possible_sets(n: int, bit_set: int) -> List[List[str]]:
            if n == 0:
                return []

            ret = []
            for i in range(1, n+1):
                if bit_set & (1 << i) == 0:
                    comb = [str(i)] * i
                    dp_i = dp_possible_sets(n-i, bit_set | (1 << i))
                    if n-i == 0:
                        ret.append(comb)
                    else:
                        for c in dp_i:
                            ret.append(comb + c)

            return ret

        n_digits_cnt = len(str(n))

        for i in range(n_digits_cnt, 8):
            possible_combs = dp_possible_sets(i, 0)
            minim = float('inf')
            for comb in possible_combs:
                for comb_ordered in set(list(permutations(comb, i))):
                    comb_ordered_int = int(''.join(comb_ordered))
                    if comb_ordered_int > n:
                        minim = min(minim, comb_ordered_int)
            if minim != float('inf'):
                return minim

        return -1
