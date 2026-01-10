from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        m_total = sum(rolls)
        n_total = ((n+m) * mean) - m_total
        avg = n_total / n
        if 1 <= avg <= 6:
            ans = [int(avg)] * n
            rem = n_total % n

            for i in range(len(ans)):
                if rem > 0:
                    ans[i] += 1
                    rem -= 1
                else:
                    break
            return ans
        else:
            return []
