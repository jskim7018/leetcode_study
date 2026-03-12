from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 위로 가면서 //2를 해주면 parent다. parent마다 반대가 되어야 한다. 그러면 정답이 나온다.

        ans = []
        while label > 0:
            ans.append(label)
            label //= 2
            if label != 0:
                smallest = (1 << (label.bit_length()-1))
                biggest = smallest * 2 - 1
                label = biggest - (label - smallest)
        ans.reverse()

        return ans
