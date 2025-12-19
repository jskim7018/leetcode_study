class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)

        prefix_sum_ones = []

        for i in range(n):
            prefix_sum_ones.append(1 if s[i] == '1' else 0)
            if i>0:
                prefix_sum_ones[i] += prefix_sum_ones[i-1]

        ans = 0
        for i in range(n):
            for j in range(i, n):
                ones_cnt = prefix_sum_ones[j]
                if i > 0:
                    ones_cnt -= prefix_sum_ones[i-1]

                zeros_cnt = (j-i+1) - ones_cnt
                if ones_cnt <= k or zeros_cnt <= k:
                    ans += 1

        return ans
