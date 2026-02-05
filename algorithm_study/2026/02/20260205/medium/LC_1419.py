from collections import defaultdict


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        curr_letter_cnt = defaultdict(int)
        ans = 0
        curr_total = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                curr_total += 1
            elif ch == 'r':
                if curr_letter_cnt['c'] > 0:
                    curr_letter_cnt['c'] -= 1
                else:
                    return -1
            elif ch == 'o':
                if curr_letter_cnt['r'] > 0:
                    curr_letter_cnt['r'] -= 1
                else:
                    return -1
            elif ch == 'a':
                if curr_letter_cnt['o'] > 0:
                    curr_letter_cnt['o'] -= 1
                else:
                    return -1
            elif ch == 'k':
                if curr_letter_cnt['a'] > 0:
                    curr_letter_cnt['a'] -= 1
                else:
                    return -1
            else:
                return -1

            if ch != 'k':
                curr_letter_cnt[ch] += 1
                ans = max(ans, curr_total)
            else:
                curr_total -= 1

        if curr_total != 0:
            return -1
        else:
            return ans
