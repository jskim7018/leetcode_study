from typing import List
from collections import defaultdict, deque


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False
        counter = defaultdict(int)
        for h in hand:
            counter[h] += 1

        sorted_dict = deque(sorted([[k, v] for k, v in counter.items()]))
        while sorted_dict:
            prev = -1
            minim = float('inf')
            size = 0
            for i in range(len(sorted_dict)):
                k = sorted_dict[i][0]
                v = sorted_dict[i][1]
                if minim == float('inf'):
                    minim = v
                if v < minim:
                    return False
                sorted_dict[i][1] -= minim
                curr = k
                if prev != -1 and curr != prev + 1:
                    return False
                prev = curr
                size += 1
                if size == groupSize:
                    break
            if size != groupSize:
                return False
            for _ in range(size):
                if sorted_dict[0][1] == 0:
                    sorted_dict.popleft()

        return True
