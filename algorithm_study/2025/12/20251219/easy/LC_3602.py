import string


class Solution:
    def concatHex36(self, n: int) -> str:
        n2 = n ** 2
        n3 = n ** 3

        def to_hexadecimal(num: int) -> str:
            digits = string.digits + string.ascii_uppercase[:6]

            ret = ''
            while num:
                num, r = divmod(num, 16)
                ret = digits[r] + ret

            return ret

        def to_hexatrigesimal(num: int) -> str:
            digits = string.digits + string.ascii_uppercase

            ret = ''
            while num:
                num, r = divmod(num, 36)
                ret = digits[r] + ret

            return ret

        return to_hexadecimal(n2) + to_hexatrigesimal(n3)
