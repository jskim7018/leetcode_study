class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target

        x = 0
        while True:
            x += 1
            next = x * (x + 1) // 2
            if next >= target and (next - target) % 2 == 0:
                break
        ans = x
        return ans
