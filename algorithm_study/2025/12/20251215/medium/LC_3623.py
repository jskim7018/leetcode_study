from typing import List
from collections import Counter


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        mod = 10**9 + 7

        def sum_formula(num: int) -> int:
            return (num*(num+1))//2

        counter = Counter()

        for p in points:
            counter[p[1]] += 1

        lines_cnt_list = []
        for v in counter.values():
            cnt = sum_formula(v-1)
            if cnt != 0:
                lines_cnt_list.append(cnt)

        print(lines_cnt_list)

        if len(lines_cnt_list) <= 1:
            return 0
        else:
            ans = 1
            for e in lines_cnt_list:
                ans *= e
                ans %= mod
            return ans

