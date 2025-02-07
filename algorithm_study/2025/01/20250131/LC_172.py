class Solution:
    def trailingZeroes(self, n: int) -> int:

        two_cnt = 0
        five_cnt = 0

        for i in range(1,n+1):
            tmp = i
            while tmp % 2 == 0:
                tmp /= 2
                two_cnt += 1
            tmp = i
            while tmp % 5 == 0:
                tmp /= 5
                five_cnt += 1

        return min(two_cnt, five_cnt)
