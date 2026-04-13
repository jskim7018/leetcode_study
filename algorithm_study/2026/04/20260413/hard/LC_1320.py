from functools import cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)

        alph_to_coord = dict()

        alph = 'A'
        for i in range(5):
            for j in range(6):
                alph_to_coord[alph] = (i, j)
                if alph == 'Z':
                    break
                alph = chr(ord(alph) + 1)

        @cache
        def dp(idx: int, y1:int, x1: int, y2: int, x2: int) -> int:
            if idx >= n:
                return 0

            coord_to_go = alph_to_coord[word[idx]]

            ret = min((dp(idx+1, coord_to_go[0], coord_to_go[1], y2, x2) +
                   abs(y1-coord_to_go[0]) + abs(x1-coord_to_go[1])),
                      (dp(idx+1, y1, x1, coord_to_go[0], coord_to_go[1]) +
                       abs(y2 - coord_to_go[0]) + abs(x2 - coord_to_go[1])))

            return ret

        ans = float('inf')

        fixed_coord = alph_to_coord[word[0]]
        for i in range(26):
            var_coord = alph_to_coord[chr(ord('A') + i)]
            ans = min(ans, dp(1, fixed_coord[0], fixed_coord[1],
                              var_coord[0], var_coord[1]))

        return ans
