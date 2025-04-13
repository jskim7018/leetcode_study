from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        @cache
        def solve(idx1, idx2, idx3) -> bool:
            if idx1 >= len(s1) and idx2 >= len(s2) and idx3 >= len(s3):
                return True

            ret = False
            if idx1 < len(s1) and idx3 < len(s3) and s1[idx1] == s3[idx3]:
                ret |= solve(idx1 + 1, idx2, idx3 + 1)
            if idx2 < len(s2) and idx3 < len(s3) and s2[idx2] == s3[idx3]:
                ret |= solve(idx1, idx2 + 1, idx3 + 1)

            return ret

        return solve(0,0,0)
