from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_mapping = defaultdict(list)

        for a in allowed:
            allowed_mapping[(a[0], a[1])].append(a[2])

        @cache
        def dp(s: str) -> bool:
            n = len(s)
            if n == 1:
                return True
            new_s = []
            def create_new_s_from_allowed(idx: int, curr_s: List[str], s: str):
                if len(curr_s) == len(s) - 1:
                    new_s.append(''.join(curr_s))
                    return

                possible = allowed_mapping[(s[idx], s[idx + 1])]

                for p in possible:
                    curr_s.append(p)
                    create_new_s_from_allowed(idx + 1, curr_s, s)
                    curr_s.pop()
            create_new_s_from_allowed(0, list(), s)
            ret = False
            for new in new_s:
                if dp(new):
                    return True
            return ret

        return dp(bottom)
