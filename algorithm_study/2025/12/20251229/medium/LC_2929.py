class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(0, min(limit + 1, n+1)):
            left_candies = n-i
            if left_candies <= limit*2:
                max_for_one = min(left_candies, limit)
                min_for_one = left_candies - max_for_one

                ans += max_for_one - min_for_one + 1

        return ans
