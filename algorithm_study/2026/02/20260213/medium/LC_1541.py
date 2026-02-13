import math


class Solution:
    def minInsertions(self, s: str) -> int:
        # 거꾸로 확인한다.
        # forward로 했도 같다. 굳이 뒤에서부터 할 필요는 없음.
        right_cnt = 0
        ans = 0
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] == ')':
                right_cnt += 1
            else:
                if right_cnt % 2 == 1:
                    right_cnt += 1
                    ans += 1
                if right_cnt == 0:
                    right_cnt += 2
                    ans += 2
                right_cnt -= 2

        if right_cnt > 0:
            if right_cnt % 2 == 1:
                right_cnt += 1
                ans += 1
            ans += right_cnt//2

        return ans
