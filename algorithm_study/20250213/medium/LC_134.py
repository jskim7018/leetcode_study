from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        curr_list = []

        for i in range(n):
            curr_list.append((gas[i] - cost[i], i))

        is_changed = True
        while is_changed:
            is_changed = False
            next_list = []
            i = 0
            while i < len(curr_list):
                if len(next_list) != 0 and next_list[-1][0] > 0 and next_list[-1][0] + curr_list[i][0] >= 0:
                    new_curr = next_list.pop()
                    next_list.append((new_curr[0] + curr_list[i][0], new_curr[1]))
                    is_changed = True
                elif curr_list[i][0] > 0 and i+1 < len(curr_list) and curr_list[i+1][0] + curr_list[i][0] >= 0:
                    next_list.append((curr_list[i+1][0] + curr_list[i][0], curr_list[i][1]))
                    i += 1
                    is_changed = True
                else:
                    next_list.append(curr_list[i])
                i += 1
            if is_changed:
                curr_list = next_list

        if len(curr_list) == 1:
            if curr_list[0][0] >= 0:
                return curr_list[0][1]
            else:
                return -1
        else:
            i = 0
            sum = 0
            while i < len(curr_list):
                sum += curr_list[i][0]
                i += 1
            if sum >= 0:
                return curr_list[-1][1]
            else:
                return -1
