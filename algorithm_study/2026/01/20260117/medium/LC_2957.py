class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        ans = 0
        i = 1
        while i < n:
            bef = ord(word[i-1])
            curr = ord(word[i])
            if abs(bef-curr) <= 1:
                ans += 1
                i += 2
            else:
                i += 1

        return ans
