class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        c_count = s.count(c)

        return (c_count*(c_count+1))//2
