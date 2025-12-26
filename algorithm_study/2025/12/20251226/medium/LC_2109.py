from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces_idx = 0

        ans = ''
        for i,ch in enumerate(s):
            if spaces_idx < len(spaces):
                if spaces[spaces_idx] == i:
                    ans += ' '
                    spaces_idx += 1
            ans += ch

        return ans
