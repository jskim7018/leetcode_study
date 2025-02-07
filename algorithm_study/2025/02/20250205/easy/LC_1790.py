class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        st1 = set()
        st2 = set()

        cnt = 0
        for c1,c2 in zip(s1,s2):
            if c1 != c2:
                cnt+=1
                if cnt > 2:
                    return False
                st1.add(c1)
                st2.add(c2)

        return st1 == st2
