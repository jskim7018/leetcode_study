from typing import List
from sortedcontainers import SortedDict


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        sortedDict = SortedDict()

        for l in lights:
            left = l[0] - l[1]
            right = l[0] + l[1] + 1

            if left in sortedDict:
                sortedDict[left] += 1
            else:
                sortedDict[left] = 1

            if right in sortedDict:
                sortedDict[right] -= 1
            else:
                sortedDict[right] = -1

        max_brightness = 0
        pos = 0
        brightness = 0
        for p, e in sortedDict.items():
            brightness += e
            if brightness > max_brightness:
                max_brightness = brightness
                pos = p

        return pos
