class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_set_bit_cnt = 0
        while num2 > 0:
            if num2 % 2 == 1:
                num2_set_bit_cnt += 1
            num2 //= 2

        ans = 0
        bit_cnt = num1.bit_count()
        origin_bit_cnt = bit_cnt
        i = 0
        while num1 > 0:
            if num1 % 2 == 1:
                if bit_cnt <= num2_set_bit_cnt:
                    ans |= 1 << i
                bit_cnt -= 1
            num1 //= 2
            i += 1
        i = 0
        num2_set_bit_cnt -= min(origin_bit_cnt, num2_set_bit_cnt)
        while num2_set_bit_cnt > 0:
            if ans & (1 << i) == 0:
                ans = ans | (1 << i)
                num2_set_bit_cnt -= 1
            i += 1
        return ans
