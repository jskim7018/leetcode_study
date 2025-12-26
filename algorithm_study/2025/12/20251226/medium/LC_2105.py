from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        
        curr_alice_cap = capacityA
        curr_bob_cap = capacityB
        refill_cnt = 0
        for i in range(n//2):
            if plants[i] > curr_alice_cap:
                curr_alice_cap = capacityA - plants[i]
                refill_cnt += 1
            else:
                curr_alice_cap -= plants[i]

            if plants[-i-1] > curr_bob_cap:
                curr_bob_cap = capacityB - plants[-i-1]
                refill_cnt += 1
            else:
                curr_bob_cap -= plants[-i-1]

        if n % 2 == 1:
            if plants[n//2] > max(curr_alice_cap, curr_bob_cap):
                refill_cnt += 1

        return refill_cnt