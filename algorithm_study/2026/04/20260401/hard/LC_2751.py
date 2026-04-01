from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # stack 사용하기.
        # 왼쪽에서 시작해서 하나씩 하기.
        # R을 stack에 넣고, L들을 만날때마다 충돌 시킴.

        ans = []
        stck = []

        robot_infos = [(p, h, d, i) for i, (p, h, d) in enumerate(zip(positions, healths, directions))]
        robot_infos.sort()

        for pos, h, d, idx in robot_infos:
            if d == 'R':
                stck.append([idx, h])
            else:
                while stck and h > 0:
                    if stck[-1][1] > h:
                        stck[-1][1] -= 1
                        if stck[-1][1] == 0:
                            stck.pop()
                        h = 0
                    elif stck[-1][1] < h:
                        h -= 1
                        stck.pop()
                    else:
                        h = 0
                        stck.pop()
                if h > 0:
                    ans.append([idx, h])

        while stck:
            ans.append(stck.pop())
        ans.sort()

        return [e[1] for e in ans]
