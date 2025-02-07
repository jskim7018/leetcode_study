class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        ans = -1
        for i in range(min(len(s1),len(s2),len(s3))):
            if s1[i] == s2[i] == s3[i]:
                ans = len(s1)-len(s1[:i+1]) + len(s2)-len(s2[:i+1]) +len(s3)-len(s3[:i+1])
            else:
                break
        return ans
