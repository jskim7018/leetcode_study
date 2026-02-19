class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # find big one. small ones are inside it.
        zeros = 0
        ones = 0
        curr = ''
        ans = 0
        for ch in s:
            if curr == '':  # First case
                curr = ch
            if ch == '0':
                if curr != '0' and zeros > 0:
                    if zeros > 0 and ones > 0:
                        ans += min(zeros, ones)
                    zeros = 0
                zeros += 1
            elif ch == '1':
                if curr != '1' and ones > 0:
                    if zeros > 0 and ones > 0:
                        ans += min(zeros, ones)
                    ones = 0
                ones += 1
            curr = ch
        if zeros > 0 and ones > 0:
            ans += min(zeros, ones)

        return ans
