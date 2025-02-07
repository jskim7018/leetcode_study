class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0

        ans = ""
        while i<len(word1) or j<len(word2):
            if i < len(word1):
                ans += word1[i]
                i+=1
            if j < len(word2):
                ans += word2[j]
                j+=1
        return ans


"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for a, b in zip(word1, word2):
            merged.append(a + b)
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return "".join(merged)
"""