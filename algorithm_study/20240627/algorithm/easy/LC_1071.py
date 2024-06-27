class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        for i in range(len(str1)):
            if len(str1) % (i+1) == 0 and len(str2) % (i+1) == 0:
                if (str1.count(str1[:i+1]) == len(str1) / (i+1)
                    and str2.count(str1[:i+1]) == len(str2) / (i+1)):
                    ans = str1[:i+1]
        return ans


"""
아래 방법으로 N만에 가능.
두 스트링을 합한게 순서 상관없이 같아야 서로를 나누는게 있다.
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
"""