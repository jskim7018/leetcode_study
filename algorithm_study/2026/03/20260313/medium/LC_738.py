import pytest


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # if right is smaller then decrease curr, and all right becomes 9s
        cnt_9s = 0

        prev = n % 10
        n //= 10
        ans = prev

        cnt = 1
        curr_digit = 1
        while n > 0:
            curr = n % 10
            if prev < curr:
                curr -= 1
                cnt_9s = cnt
                curr_digit = 0
                ans = 0
            ans += curr * pow(10, curr_digit)
            curr_digit += 1
            prev = curr
            cnt += 1

            n //= 10

        for _ in range(cnt_9s):
            ans = ans * 10 + 9

        return ans


@pytest.mark.parametrize("input_n, expected", [
    (10, 9),
    (1234, 1234),
    (332, 299),
    (105, 99)
])
def test_monotoneIncreasingDigits(input_n, expected):
    sol = Solution()
    assert sol.monotoneIncreasingDigits(input_n) == expected
