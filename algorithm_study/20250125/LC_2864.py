class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_cnt = s.count('1')

        ans = ['0'] * len(s)

        for i in range(one_cnt-1):
            ans[i] = '1'

        ans[len(ans)-1] = '1'

        return ''.join(ans)
