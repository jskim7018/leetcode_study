from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        st = set(nums)

        ans = ""
        def solve(idx, curr) -> bool:
            nonlocal ans

            if idx >= n:
                if curr not in st:
                    ans = curr
                    return True
                return False


            ret = solve(idx+1, curr + "0")
            if ret:
                return ret
            ret = solve(idx+1, curr + "1")
            if ret:
                return ret

        solve(0, "")
        return ans
