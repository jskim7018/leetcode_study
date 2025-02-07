# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = 2**31 - 1
        pick = (l+r) / 2

        while l<=r:
            if guess(pick) == 0:
                return int(pick)
            elif guess(pick) == -1:
                r = pick-1
            else:
                l = pick+1
            pick = (l+r)/2

        return pick