class Solution:
    def possibleStringCount(self, word: str) -> int:

        ans = 1

        cnt = 1
        i = 1
        while i < len(word):
            if word[i] == word[i-1]:
                cnt += 1
            else:
                ans += cnt-1
                cnt = 1
            i += 1
        ans += cnt-1
        return ans
