from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s_list = list(s)

        ans = 0

        def get_points(rem_str: str, points: int) -> List[str]:
            nonlocal ans
            new_s = []
            i = 0
            while i < len(s_list):
                if s_list[i] == rem_str[1] \
                        and new_s and new_s[-1] == rem_str[0]:
                    new_s.pop()
                    ans += points
                else:
                    new_s.append(s_list[i])
                i += 1
            return new_s

        if x >= y:
            new_s = get_points("ab", x)
            s_list = list(new_s)
            get_points("ba", y)
        else:
            new_s = get_points("ba", y)
            s_list = list(new_s)
            get_points("ab", x)

        return ans