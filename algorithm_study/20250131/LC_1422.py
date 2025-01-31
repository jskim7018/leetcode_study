class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')

        ans = 0
        zero_cnt = 0
        ones_cnt = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zero_cnt += 1
            else:
                ones_cnt += 1
            ans = max(ans, zero_cnt + (total_ones - ones_cnt))

        return ans
