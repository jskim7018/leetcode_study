class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def solve(idx, prev, cnt):
            if idx >= n and cnt >= 2:
                return True
            if idx >= n:
                return False

            is_possible = False
            for i in range(idx,n):
                num = int(s[idx:i+1])
                if idx != 0:
                    if num != prev-1:
                        continue
                is_possible |= solve(i+1, num, cnt+1)

            return is_possible

        return solve(0, 0, 0)
