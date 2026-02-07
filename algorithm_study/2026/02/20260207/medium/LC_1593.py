from functools import cache


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        curr_st = set()

        @cache
        def sub_str_cache(start, end) -> str:
            return s[start: end + 1]

        def backtracking(idx: int) -> int:
            if idx >= n:
                return 0
            ret = 0
            for i in range(idx, n):
                substr = sub_str_cache(idx, i)
                if substr in curr_st:
                    continue
                else:
                    curr_st.add(substr)
                    ret = max(ret, backtracking(i+1)+1)
                    curr_st.remove(substr)
            return ret

        return backtracking(0)
