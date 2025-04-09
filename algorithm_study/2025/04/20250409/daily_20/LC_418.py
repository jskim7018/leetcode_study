from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        s_total_length = n

        for s in sentence:
            s_total_length += len(s)

        curr_idx = 0
        ans = 0
        for _ in range(rows):
            curr_left_cols = cols
            if curr_left_cols >= s_total_length-1:
                ans += (curr_left_cols+1)//s_total_length * n
                curr_left_cols += 1
                curr_left_cols %= s_total_length
                curr_left_cols -= 1

            while curr_left_cols > 0:
                if curr_left_cols >= len(sentence[curr_idx]):
                    curr_left_cols -= len(sentence[curr_idx]) + 1
                    ans += 1
                    curr_idx += 1
                    curr_idx %= n
                else:
                    break
        ans //= n
        return ans
