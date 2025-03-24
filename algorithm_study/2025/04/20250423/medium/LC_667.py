from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        l = 1
        r = n

        i = 0
        is_curr_small = False
        ans = []
        while i < n:
            if k > 0:
                if is_curr_small:
                    ans.append(r)
                    r -= 1
                else:
                    ans.append(l)
                    l += 1
                is_curr_small = not is_curr_small
                k-=1
            else:
                if is_curr_small:
                    ans += range(l, r+1)
                else:
                    ans += range(r, l-1, -1)
                break
            i += 1

        return ans
