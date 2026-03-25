class Solution:
    def rotatedDigits(self, n: int) -> int:
        # 3, 4, 7가 없으면서
        # 2,5,6,9 하나라도 있어야 함.
        # brute force 가능

        ans = 0
        for i in range(1, n+1):
            str_num = str(i)

            possible = False
            for ch in str_num:
                if ch == '2' or ch == '5' or ch == '6' or ch == '9':
                    possible = True
                elif ch == '3' or ch == '4' or ch == '7':
                    possible = False
                    break
            if possible:
                ans += 1

        return ans
