from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)

        dec_cnt_from_left = [1] * n
        dec_cnt_from_right = [1] * n

        for i in range(1, len(security)):
            if security[i - 1] >= security[i]:
                dec_cnt_from_left[i] += dec_cnt_from_left[i - 1]
            if security[-i] >= security[-i - 1]:
                dec_cnt_from_right[-i - 1] += dec_cnt_from_right[-i]

        ans = []
        for i in range(time, n-time):
            left = i - time
            right = i + time
            if left < 0 or right >= n:
                continue
            else:
                if dec_cnt_from_left[i] - 1 >= time and \
                        dec_cnt_from_right[i] - 1 >= time:
                    ans.append(i)
        return ans
