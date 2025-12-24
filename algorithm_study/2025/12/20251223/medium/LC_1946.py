from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        change_mp = {str(i): str(ch) for i, ch in enumerate(change)}
        ans = ''

        is_change_start = False
        last_idx = len(num)
        for i, ch in enumerate(num):
            if change_mp[ch] > ch:
                ans += change_mp[ch]
                is_change_start = True
            elif change_mp[ch] == ch:
                ans += ch
            elif is_change_start:
                last_idx = i
                break
            else:
                ans += ch

        ans += num[last_idx:]

        return ans
