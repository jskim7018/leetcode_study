import math


class Solution:
    def minSwaps(self, s: str) -> int:
        cnt_left = 0
        cnt_right = 0
        for ch in s:
            if ch == '[':
                cnt_left += 1
            else:
                if cnt_left > 0:
                    cnt_left -= 1
                else:
                    cnt_right += 1

        return math.ceil(cnt_right / 2)
