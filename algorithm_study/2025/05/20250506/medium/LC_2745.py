class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        ans = z
        maxim = max(x,y)
        minim = min(x,y)

        if minim == maxim:
            ans += minim*2
        else:
            ans += minim + minim+1
        ans *= 2

        return ans
