class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_cnt = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                a_cnt += 1

        curr_b_delete = 0
        curr_a_cnt = 0
        ans = float('inf')
        for i, ch in enumerate(s):
            if ch == 'b':
                ans = min(ans, a_cnt - curr_a_cnt + curr_b_delete)
                curr_b_delete += 1
            else:
                curr_a_cnt += 1
        ans = min(ans, curr_b_delete)

        if ans == float('inf'):
            return 0
        else:
            return ans
