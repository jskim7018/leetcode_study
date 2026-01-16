from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []

        def dfs(curr_num: int, digit_cnt: int):
            if digit_cnt == n:
                ans.append(curr_num)
                return

            if digit_cnt == 0:
                for i in range(1, 10):
                    dfs(i, digit_cnt + 1)
            else:
                last_digit = curr_num % 10
                left = last_digit - k
                right = last_digit + k
                if 0 <= left <= 9:
                    dfs(curr_num * 10 + left, digit_cnt + 1)
                if 0 <= right <= 9 and left != right:
                    dfs(curr_num * 10 + right, digit_cnt + 1)

        dfs(-1, 0)

        return ans
