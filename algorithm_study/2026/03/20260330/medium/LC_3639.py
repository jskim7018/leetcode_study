from typing import List
from sortedcontainers import SortedSet


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        # *로 바꾸는 것은 일종의 쪼개기.
        # 쪼개면서 valid 하지 않은 것들 갯수 유지. (valid 한것은=[전체 - (non_valid)])>=k인지 확인.
        # 전체 갯수가 시작부터 k보다 작으면 불가능.
        def substr_cnt(length: int) -> int:
            return (length*(length+1))//2

        n = len(s)

        total = substr_cnt(n)
        curr_invalid_cnt = total

        if total < k:
            return -1

        sorted_set = SortedSet()

        for t in range(n):
            o_idx = order[t]

            l = 0
            r = n-1

            r_idx = sorted_set.bisect_right(o_idx)
            l_idx = sorted_set.bisect_right(o_idx) - 1

            if 0 <= l_idx < len(sorted_set):
                l = sorted_set[l_idx] + 1
            if 0 <= r_idx < len(sorted_set):
                r = sorted_set[r_idx] - 1

            curr_invalid_cnt -= substr_cnt(r-l+1)

            mid = o_idx
            curr_invalid_cnt += substr_cnt((mid-1) - l + 1) + substr_cnt(r-(mid+1) + 1)
            if total - curr_invalid_cnt >= k:
                return t
            sorted_set.add(o_idx)

        return -1
