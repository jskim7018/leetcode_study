class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        while (k - 1) / 26 <= (n - 1) and n - 1 >= 0:
            ans.append('a')
            n -= 1
            k -= 1

        z_cnt = k // 26
        left_over = k % 26
        if left_over != 0:
            ans.append(chr(left_over-1+ord('a')))
        for _ in range(z_cnt):
            ans.append('z')

        return ''.join(ans)
