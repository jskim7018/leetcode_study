class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = high - low + 1

        ans = cnt//2

        if cnt % 2 == 1 and low % 2 == 1:
            ans += 1

        return ans