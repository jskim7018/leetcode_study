from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)

        chosen = []
        ans = []

        def dp(idx):
            nonlocal ans
            nonlocal chosen

            if len(chosen) == 4 and idx >= n:
                ans.append('.'.join(chosen))
                return
            if len(chosen) >= 4:
                return

            for end in range(idx, idx+3):
                if end < n:
                    ip_segment = s[idx:end+1]
                    if len(ip_segment) != 1 and ip_segment[0] == '0':
                        continue
                    if int(ip_segment) <= 255:
                        chosen.append(ip_segment)
                        dp(end+1)
                        chosen.pop()

        dp(0)
        return ans
