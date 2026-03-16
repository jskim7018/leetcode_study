class Solution:
    def countCommas(self, n: int) -> int:
        # If n is less than 1000 then answer is 0

        curr = 1_000
        comma_cnt = 1

        ans = 0
        while n >= curr:
            ans += comma_cnt * ((min((curr*1000)-1, n)+1) - curr)
            curr *= 10**3
            comma_cnt += 1

        return ans
