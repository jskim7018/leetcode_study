class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # TODO: 그냥 단순 exp 왜 느리지???
        #  => 10^5*log*log 느림. log/constant도 여러번 곱하면 커짐.

        mod = 10**9 + 7

        ans = 0
        for num in range(1, n+1):
            ans = ((ans << num.bit_length()) | num) % mod

        return ans
