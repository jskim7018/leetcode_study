from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        sweep = [0] * n

        # preprocess sweep for line sweeping
        for sh in shifts:
            start, end, direction = sh
            if direction == 0:
                direction = -1
            sweep[start] += direction
            if end + 1 < n:
                sweep[end+1] += -direction

        # line sweep
        ans = []
        sweep_accum = 0
        for i, ch in enumerate(s):
            sweep_accum += sweep[i]

            alph_num = ord(ch) - ord('a')
            alph_num += sweep_accum
            ans.append(chr(alph_num % 26 + ord('a')))

        return ''.join(ans)
