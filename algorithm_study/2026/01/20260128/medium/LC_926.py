class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)

        zeros = s.count('0')

        ans = zeros
        curr_ones = 0
        for i in range(n):
            if s[i] == '0':
                zeros -= 1
            else:
                curr_ones += 1

            ans = min(ans, curr_ones + zeros)

        return ans
