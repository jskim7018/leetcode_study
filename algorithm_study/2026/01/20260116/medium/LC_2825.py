class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        str1_n = len(str1)
        str2_n = len(str2)

        def canMakeSubsequenceWithDiff(diff: int) -> bool:
            str1_idx = 0
            str2_idx = 0

            while str1_idx < str1_n and str2_idx < str2_n:
                ch1 = ord(str1[str1_idx]) - ord('a')
                ch2 = ord(str2[str2_idx]) - ord('a')
                if ch1 == ch2 or ((ch1 + diff) % 26 + 26) % 26 == ch2:
                    str2_idx += 1

                str1_idx += 1

            if str2_idx >= str2_n:
                return True
            else:
                return False

        return canMakeSubsequenceWithDiff(1)
