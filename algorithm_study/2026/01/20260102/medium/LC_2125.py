from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for b in bank:
            device_cnt = b.count('1')
            if device_cnt == 0:
                continue
            ans += prev * device_cnt
            prev = device_cnt

        return ans
