class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def solve(number: str) -> int:
            number_len = len(number)
            number_int = int(number)
            s_len = len(s)
            s_int = int(s)
            if number_int == 0:
                return 0
            elif number_int < s_int:
                return 0
            elif number_int >= s_int and number_len == s_len:
                return 1

            first_digit = int(number[0])
            diff = number_len - s_len - 1 # check digit count difference
            ret = min(first_digit, limit)
            tmp = ret
            if ret != first_digit:
                ret += 1
            # get combinations if number is 5678 and s is 55 diff will be 2.
            for _ in range(diff):
                ret *= (limit+1)

            # if limit is smaller we can finish right away
            # or else we recursively check next number as below
            if tmp == first_digit:
                ret += solve(number[1:])
            return ret

        ans = solve(str(finish)) - solve(str(start-1))
        return ans
