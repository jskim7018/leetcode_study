from typing import List


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        st = set(bannedWords)

        cnt = 0
        for m in message:
            if m in st:
               cnt += 1
            if cnt >= 2:
                return True
        return False