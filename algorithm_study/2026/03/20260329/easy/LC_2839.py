class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        for i in range(4):
            if (s1[i] != s2[i] and
            s1[i] != s2[(i+2)%4]):
                return False
        return True
