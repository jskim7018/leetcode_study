
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        mult = 1
        ans = 0
        for c in columnTitle[::-1]:
            print(c)
            ans += ((ord(c)-ord('A') + 1) * mult)
            mult *= 26

        return ans
