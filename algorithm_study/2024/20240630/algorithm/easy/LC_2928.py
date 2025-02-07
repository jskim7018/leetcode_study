class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        n+=2 # 막대기 공간 추가
        # 3중 for 문으로
        for i in range(n-1):
            for j in range(i+1, n):
                if i <= limit and j-i - 1 <= limit and n -j - 1 <= limit:
                    ans += 1
        return ans

"""
Using venn diagram concept:
ref: https://leetcode.com/problems/distribute-candies-among-children-i/solutions/4276967/python-3-8-lines-include-exclude-t-s-97-99/
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
         
        ans =   (n+2)*(n+1)//2

        if (n:= n - limit-1) < 0: return ans
        ans-= 3*(n+2)*(n+1)//2

        if (n:= n - limit-1) < 0: return ans
        ans+= 3*(n+2)*(n+1)//2

        if (n:= n - limit-1) < 0: return ans
        ans-=   (n+2)*(n+1)//2

        return ans
"""