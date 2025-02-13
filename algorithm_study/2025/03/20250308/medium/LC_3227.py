class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_cnt = 0
        vowel_st = set("aeiou")

        for c in s:
            if c in vowel_st:
                return True

        return False
