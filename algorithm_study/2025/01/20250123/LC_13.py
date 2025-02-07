class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        val = 0

        idx = len(s)-1
        while idx >= 0:
            curr_val = mp[s[idx]]
            if idx-1 >= 0 and mp[s[idx-1]] < curr_val:
                curr_val -= mp[s[idx-1]]
                idx -= 1

            val += curr_val

            idx -= 1

        return val
