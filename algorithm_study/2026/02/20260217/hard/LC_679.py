from typing import List, Set
from fractions import Fraction
from itertools import permutations
from functools import cache


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # 가능 한것들 1. (a @ b) @ (c @ d), 2. a @ ((b @ c) @ d),
        # 3. a @ (b @ (c @ d)) 4. ((a @ b) @ c) @ d, 5. (a @ (b @ c)) @ d
        # 생각보다 경우의 수가 얼마 없음.
        # 완탐으로 가능함. 나눗셈을 고려하여 모두 Fraction화 하여 한다?
        # Catalan Number. TODO: Backtracking. 2개 선택해서 연산 후 val 배열에 넣어주고 continue, 1개 남으면 확인.

        n = len(cards)
        @cache
        def all_results(curr_cards, l: int, r: int) -> frozenset:
            if l == r:
                return frozenset({Fraction(curr_cards[l], 1)})

            ret = set()

            for i in range(l, r):
                left = all_results(curr_cards, l, i)
                right = all_results(curr_cards, i+1, r)

                for fract1 in left:
                    for fract2 in right:
                        ret.add(fract1 + fract2)
                        ret.add(fract1 - fract2)
                        ret.add(fract1 * fract2)
                        if fract2 != 0:
                            ret.add(fract1 / fract2)
            return ret

        for perm in permutations(cards):
            results = all_results(perm, 0, n - 1)
            for fract in results:
                if (fract.numerator == 24 and
                        fract.denominator == 1):
                    return True
        return False
