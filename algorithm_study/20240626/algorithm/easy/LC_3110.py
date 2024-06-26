class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans += abs(ord(s[i-1]) - ord(s[i]))
        return ans

"""
ref: https://leetcode.com/problems/score-of-a-string/editorial/

# Can use pairwise for getting pairs
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a,b in pairwise(s))
"""