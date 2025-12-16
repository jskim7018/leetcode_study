class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        cnt_a = 0
        cnt_b = 0

        for c in s:
            if c == 'a':
                cnt_a += 1
            else:
                cnt_b += 1

        return abs(cnt_a-cnt_b)
