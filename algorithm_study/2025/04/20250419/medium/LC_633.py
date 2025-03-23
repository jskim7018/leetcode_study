class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrs_st = set()
        for i in range(int(c**0.5)+1):
            sqrs_st.add(i*i)
        for a in range(0, int(c**0.5 + 1)):
           b = c - a**2
           if b in sqrs_st:
               return True
        return False
