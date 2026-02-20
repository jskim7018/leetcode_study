class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # n이 작아서 완탐 가능.
        n = len(s)

        def is_special_str(_s: str) -> bool:
            ones = 0
            zeros = 0
            ret = True
            for ch in _s:
                if ch == '0':
                    zeros += 1
                else:
                    ones += 1
                if zeros > ones:
                    ret = False
            if ones != zeros:
                ret = False

            return ret
        ans = s
        for _ in range(n//2):
            for i in range(n-1):  # 시작.
                for j in range(i+1, n):  # 끝.
                    for k in range(i+1, j+1):  # 중간.
                        left, right = s[i:k], s[k:j+1]
                        if is_special_str(left) and is_special_str(right):
                            ans = max(ans, s[:i] + right + left + s[j+1:])
            s = ans
        return s
