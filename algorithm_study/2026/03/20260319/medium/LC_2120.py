from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directions = {
            "R": (0,1),
            "L": (0,-1),
            "U": (-1,0),
            "D": (1,0)
        }

        s_n = len(s)
        ans = []


        ey, ex = startPos
        e_idx = 0
        cnt = 0
        for i in range(s_n):
            while e_idx < s_n:
                dy, dx = directions[s[e_idx]]
                ny = ey + dy
                nx = ex + dx
                if ny < n and nx < n and ny >= 0 and nx >= 0:
                    ey = ny
                    ex = nx
                    e_idx += 1
                else:
                    break
            ans.append(e_idx - i)
            dy, dx = directions[s[i]]
            ey -= dy
            ex -= dx
            cnt -= 1

        return ans
