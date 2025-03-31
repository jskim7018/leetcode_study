class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while maxDoubles:
            if target == 1:
                return ans
            if target % 2 == 1:
                target -= 1
                ans += 1
            target //= 2
            maxDoubles -= 1
            ans += 1

        if target == 1:
            return ans
        else:
            return ans + target - 1
