class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # sliding window. window should have min with k or less.
        n = len(answerKey)
        l = 0
        true_cnt = 0
        false_cnt = 0

        ans = 0
        for r in range(n):
            if answerKey[r] == 'T':
                true_cnt += 1
            else:
                false_cnt += 1

            while min(true_cnt, false_cnt) > k:
                if answerKey[l] == 'T':
                    true_cnt -= 1
                else:
                    false_cnt -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans
