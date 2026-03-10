from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        ans = []
        j = 0

        is_possible = True
        while is_possible:
            need = ""
            is_possible = True
            for i in range(n):
                if j >= len(strs[i]):
                    is_possible = False
                    break
                if i == 0:
                    need = strs[i][j]
                else:
                    if need != strs[i][j]:
                        is_possible = False
                        break
            if is_possible:
                ans.append(need)
            j += 1

        return ''.join(ans)
