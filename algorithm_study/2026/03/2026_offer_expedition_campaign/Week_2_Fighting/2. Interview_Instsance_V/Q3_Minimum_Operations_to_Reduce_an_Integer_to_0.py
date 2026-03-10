class Solution:
    def minOperations(self, n: int) -> int:
        # 1이 1개 독립적으로 있으면 그냥 한번
        # 1이 2개 이상 연속으로 있으면 무조건 2번만 하면됨.
        # 101 -> 2번
        # 11011 -> 3번
        # 110011 -> 4번

        ans = 0
        curr_ones = 0
        is_prev_zero = False
        while n > 0:
            bit = n % 2
            if bit == 1:
                if is_prev_zero and curr_ones > 1:
                    ans += 1
                curr_ones += 1
                is_prev_zero = False
            elif bit == 0:
                if curr_ones == 1:
                    ans += 1
                    curr_ones = 0
                elif curr_ones > 1:
                    if is_prev_zero:
                        ans += 2
                        curr_ones = 0
                is_prev_zero = True
            n //= 2

        if curr_ones == 1:
            ans += 1
        elif curr_ones > 1:
            ans += 2
        return ans
