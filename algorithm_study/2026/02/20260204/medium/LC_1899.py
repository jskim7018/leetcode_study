from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible = [False] * 3

        for triplet in triplets:
            curr_possible = [False] * 3
            is_okay = True
            for i, (a, t) in enumerate(zip(triplet, target)):
                if a == t:
                    curr_possible[i] = True
                elif a > t:
                    is_okay = False
            if is_okay:
                curr_result = True
                for i in range(3):
                    possible[i] |= curr_possible[i]
                    curr_result &= possible[i]

                if curr_result:
                    return True
        return False

