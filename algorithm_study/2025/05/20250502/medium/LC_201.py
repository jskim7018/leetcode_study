class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:


        ans = 0
        for i in range(30, -1, -1):
            bit_bef = 1 << (i+1)
            bit_aft = 1 << i
            if left >= bit_aft and right < bit_bef:
                ans |= bit_aft
                left -= bit_aft
                right -= bit_aft
        return ans
