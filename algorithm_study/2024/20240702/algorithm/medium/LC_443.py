from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_c = ''
        cnt = 0
        curr_idx = 0
        for i in range(0, len(chars)+1):
            cnt += 1
            if i == len(chars):
                break
            if i == 0 or (i < len(chars)-1 and chars[i] == chars[i+1]):
                curr_c = chars[i]
            if i >= len(chars)-1 or chars[i] != chars[i+1]:
                chars[curr_idx] = chars[i]
                curr_idx += 1
                if cnt >= 2:
                    for c in str(cnt):
                        chars[curr_idx] = c
                        curr_idx += 1
                cnt = 0

        return curr_idx
