from typing import List
from functools import cache, lru_cache


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)

        @cache
        def get_comp_score(st_idx: int, mentor_idx: int) -> int:
            score = 0
            for x, y in zip(students[st_idx], mentors[mentor_idx]):
                if x == y:
                    score += 1
            return score

        @lru_cache(None)
        def get_max_comp_sum(st_idx: int, mentor_st_mask: int) -> int:
            if st_idx >= m:
                return 0

            ret = 0
            for m_idx in range(m):
                if mentor_st_mask & (1 << m_idx) == 0:
                    mentor_st_mask |= (1 << m_idx)
                    ret = max(ret, get_max_comp_sum(st_idx+1, mentor_st_mask)
                              + get_comp_score(st_idx, m_idx))
                    mentor_st_mask ^= (1 << m_idx)
            return ret

        return get_max_comp_sum(0,0)
