class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        nines_cnt, rem = divmod(sum, 9)

        need_num_cnt = nines_cnt + (1 if rem > 0 else 0)

        if need_num_cnt > num:
            return ""
        else:
            ans = "9" * nines_cnt
            if rem > 0:
                ans += str(rem)
            need_zero_cnt = num-need_num_cnt
            ans += "0" * need_zero_cnt

            return ans
